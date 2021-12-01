"""
Advent of code, day 11 - Seating System

https://adventofcode.com/2020/day/11
"""
import fileinput
import copy
import itertools
from collections import Counter


if __name__ == "__main__":
    layout = []
    for line in fileinput.input():
        layout.append([char for char in line.strip()])
    width = len(layout[0]) - 1
    length = len(layout) - 1

    neighbours = copy.deepcopy(layout)
    # Neighbours for set 1
    for r in range(len(layout)):
        for c in range(len(layout[0])):
            neighbours[r][c] = set()
            for rs, cs in itertools.product((-1, 0, 1), (-1, 0, 1)):
                pos = r + rs, c + cs
                if (pos[0] < 0) or (pos[0] > length - 1):
                    continue
                if (pos[1] < 0) or (pos[1] > width - 1):
                    continue

                if layout[pos[0]][pos[1]] == "L":
                    neighbours[r][c].add(pos)
                    break

            if (r, c) in neighbours[r][c]:
                neighbours[r][c].remove((r, c))

    # Neighbours for set 2
    for r in range(len(layout)):
        for c in range(len(layout[0])):
            neighbours[r][c] = set()
            for rs, cs in itertools.product((-1, 0, 1), (-1, 0, 1)):
                for step in range(1, max(length, width)):
                    pos = r + step * rs, c + step * cs
                    if (
                        (pos[0] < 0)
                        or (pos[0] > length)
                        or (pos[1] < 0)
                        or (pos[1] > width)
                    ):
                        continue

                    if layout[pos[0]][pos[1]] == "L":
                        neighbours[r][c].add(pos)
                        break

            if (r, c) in neighbours[r][c]:
                neighbours[r][c].remove((r, c))

    while True:
        new_layout = copy.deepcopy(layout)

        for ri in range(len(layout)):
            for ci in range(width + 1):
                # if (ri == 0) and (ci == 6):
                # print(ri, ci, layout[ri][ci], neighbours[ri][ci])
                if layout[ri][ci] == "L":
                    if sum(
                        layout[nri][nci] != "#" for nri, nci in list(neighbours[ri][ci])
                    ) == len(neighbours[ri][ci]):
                        new_layout[ri][ci] = "#"

                if layout[ri][ci] == "#":
                    if (
                        sum(
                            layout[nri][nci] == "#"
                            for nri, nci in list(neighbours[ri][ci])
                        )
                        > 4
                    ):
                        new_layout[ri][ci] = "L"

        new_l = "\n".join("".join(r) for r in new_layout)
        old_l = "\n".join("".join(r) for r in layout)

        if old_l == new_l:
            print(Counter(new_l)["#"], "occupied seats")
            break
        layout = copy.deepcopy(new_layout)
