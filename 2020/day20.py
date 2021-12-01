"""
Advent of code, day 20 - Jurassic Jigsaw

https://adventofcode.com/2020/day/20
"""
import sys
import itertools
import collections
import math
import numpy as np

Directions = collections.namedtuple("Directions", ["north", "east", "west", "south"])


class Tile:
    def __init__(self, l, id=None, related=None, related_edges=None):
        self.a = np.array(l)
        self.id = id
        self.related = related if related else set()
        self.related_edges = related_edges if related_edges else dict()

    def top(self):
        return int("".join(self.a[0, :]).replace(".", "0").replace("#", "1"), base=2)

    def topbw(self):
        return int(
            "".join(reversed(self.a[0, :])).replace(".", "0").replace("#", "1"), base=2
        )

    def rightbw(self):
        return int(
            "".join(reversed(self.a[:, -1])).replace(".", "0").replace("#", "1"), base=2
        )

    def right(self):
        return int("".join(self.a[:, -1]).replace(".", "0").replace("#", "1"), base=2)

    def bottombw(self):
        return int("".join(self.a[-1, :]).replace(".", "0").replace("#", "1"), base=2)

    def bottom(self):
        return int(
            "".join(reversed(self.a[-1, :])).replace(".", "0").replace("#", "1"), base=2
        )

    def left(self):
        return int(
            "".join(reversed(self.a[:, 0])).replace(".", "0").replace("#", "1"), base=2
        )

    def leftbw(self):
        return int("".join(self.a[:, 0]).replace(".", "0").replace("#", "1"), base=2)

    def edges(self):
        return [
            self.top(),
            self.topbw(),
            self.left(),
            self.leftbw(),
            self.right(),
            self.rightbw(),
            self.bottom(),
            self.bottombw(),
        ]

    def neighbour_directions(self):
        return Directions(
            self.related_edges.get(self.top()),
            self.related_edges.get(self.right()),
            self.related_edges.get(self.left()),
            self.related_edges.get(self.bottom()),
        )

    def __repr__(self):
        return "Tile<" + str(self.id) + ">"

    def __str__(self):
        return str(self.a)

    def add_related_edge(self, other, edge):
        self.related.add(other)
        self.related_edges[edge] = other

    def num_related(self):
        return len(self.related)

    def rotate90(self):
        self.a = np.rot90(self.a)

    def flipud(self):
        self.a = np.flipud(self.a)

    def fliplr(self):
        self.a = np.fliplr(self.a)


def parse_tiles(lines):
    tiles = {}
    tile = []
    id = None
    for line in lines:
        if line == "\n":
            tiles[id] = Tile(tile, id=id)
            tile = []
        elif line.startswith("Tile "):
            id = int(line.strip().split("Tile ")[1][:-1])
        else:
            tile.append([c for c in line.strip()])
    if tile:
        tiles[id] = Tile(tile, id=id)
    return tiles


def rotate_and_flip_until(t, d):
    # print("start", t.neighbour_directions(), "target", d)
    while d.south and t.neighbour_directions().south is None:
        t.rotate90()
        # print("rotate", t.neighbour_directions())

    while d.east and t.neighbour_directions().east is None:
        t.fliplr()
        # print("fliplr", t.neighbour_directions())

    # print("end", t.neighbour_directions())


def permute(t):
    for i in range(8):
        if i == 4:
            t.flipud()
            yield t
        else:
            t.rotate90()
            yield t


def form_grid(tiles):
    n = int(len(tiles) ** 0.5)
    grid = {}

    side = 10
    img = np.zeros((n * side, n * side), dtype=object)

    tile = [t for t in tiles.values() if t.num_related() == 2][0]
    grid[(0, 0)] = tile

    rotate_and_flip_until(grid[(0, 0)], Directions(None, True, None, True))

    img[0:10, 0:10] = tile.a

    # First row in image:
    for col in range(1, n):
        for neighbour in tile.related:
            for neighbout in permute(neighbour):
                if "".join(img[0:10, side * col - 1]) == "".join(neighbout.a[:, 0]):
                    img[0:10, side * col : side * (col + 1)] = neighbout.a
                    grid[(0, col)] = neighbout
                    tile = neighbout

    # for each column in the image thereafter
    for col in range(0, n):
        tile = grid[(0, col)]

        for row in range(1, n):
            for neighbour in tile.related:
                for neighbout in permute(neighbour):
                    if "".join(
                        img[row * side - 1, col * side : (col + 1) * side]
                    ) == "".join(neighbout.a[0, :]):
                        img[
                            row * side : (row + 1) * side, side * col : side * (col + 1)
                        ] = neighbout.a
                        grid[(row, col)] = neighbout
                        tile = neighbout

    img_no_borders = np.empty((n * side - 2 * n, n * side - 2 * n), dtype=object)

    # Remove "join lines"
    for i, j in itertools.product(range(n), range(n)):
        img_no_borders[i * 8 : (i + 1) * 8, j * 8 : (j + 1) * 8] = img[
            (i * 10 + 1) : ((i + 1) * 10 - 1), (j * 10 + 1) : ((j + 1) * 10 - 1)
        ]
    # s = "\n".join("".join(str(c) for c in row) for row in img_no_borders)

    monster = np.array(
        (
            list("                  # "),
            list("#    ##    ##    ###"),
            list(" #  #  #  #  #  #   "),
        )
    )
    monster_pos = {(x, y) for y, x in zip(*np.where(monster == "#"))}
    monster_width = len(monster[0])
    monster_height = len(monster)
    image_size = n * 8

    monster_found = False
    for i in range(8):
        # Rough water positions need to be calculated after every rotation or flip.
        all_rough_water_pos = {(x, y) for y, x in zip(*np.where(img_no_borders == "#"))}
        for y in range(image_size - monster_height):
            for x in range(image_size - monster_width):
                cropped = img_no_borders[y : y + monster_height, x : x + monster_width]
                rough_water_pos = set()
                for cy, row in enumerate(cropped):
                    for cx, char in enumerate(row):
                        if char == "#":
                            rough_water_pos.add((cx, cy))
                if monster_pos.issubset(rough_water_pos):
                    monster_found = True
                    for x_, y_ in monster_pos & rough_water_pos:
                        pos = (x + x_, y + y_)
                        all_rough_water_pos.remove(pos)
        if monster_found:
            break
        img_no_borders = np.rot90(img_no_borders)
        if i == 4:
            img_no_borders = np.flip(img_no_borders, 1)

    return len(all_rough_water_pos)


if __name__ == "__main__":
    tiles = parse_tiles(sys.stdin.readlines())

    # Add matching edges
    for tile1, tile2 in itertools.product(tiles.values(), tiles.values()):
        if tile1.id == tile2.id:
            continue
        for e1 in tile1.edges():
            for e2 in tile2.edges():
                if e1 == e2:
                    tile1.add_related_edge(tile2, e1)
                    tile2.add_related_edge(tile1, e2)

    print("Part 1:", math.prod(id for id, t in tiles.items() if t.num_related() == 2))

    num_monsters = form_grid(tiles)
    print("Part 2:", num_monsters)
