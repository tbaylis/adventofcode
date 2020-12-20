"""
Advent of code, day 20 - Jurassic Jigsaw

https://adventofcode.com/2020/day/20
"""
import sys
import itertools
import collections
import math

class Tile(list):
    id = None

    def __init(self, *args, id=None):
        super().__init__(*args)
        self.id = id

    @property
    def top(self):
        return self[0]

    @property
    def right(self):
        return ''.join(row[-1] for row in self)

    @property
    def bottom(self):
        return self[-1][::-1]

    @property
    def left(self):
        return ''.join(row[0] for row in self[::-1])

    # @property
    def edges(self):
        original = [self.top, self.left, self.right, self.bottom]
        return original + [''.join(reversed(o)) for o in original]

    def __str__(self):
        return '\n'.join(str(''.join(c for c in row)) for row in self)

def parse_tiles(lines):
    tiles = {}
    tile = []
    id = None
    for line in lines:
        if line == '\n':
            tiles[id] = Tile(tile, id=id)
            tile = []
        elif line.startswith('Tile '):
            id = int(line.strip().split('Tile ')[1][:-1])
        else:
            tile.append([c for c in line.strip()])
    if tile:
        tiles[id] = Tile(tile, id=id)
    return tiles

if __name__ == "__main__":
    tiles = parse_tiles(sys.stdin.readlines())

    matching = collections.defaultdict(lambda: set())

    for (id1, t1), (id2, t2) in itertools.product(tiles.items(), tiles.items()):
        if id1 == id2:
            continue

        for i1, s1i in enumerate(t1.edges()):
            for i2, s2i in enumerate(t2.edges()):
                if s1i == s2i:
                    matching[id1].add(id2)
                elif s1i == ''.join(reversed(s2i)):
                    matching[id1].add(id2)

    print("Part 1:", math.prod(id for id, v in matching.items() if len(v) == 2))
