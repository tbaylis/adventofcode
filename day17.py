"""
Advent of code, day 17 - Conway Cubes

https://adventofcode.com/2020/day/17
"""
import fileinput
import sys
import collections
import itertools
import copy


class Grid:
    def __init__(self, initial, dimensions=3):
        self.active = collections.defaultdict(lambda: False)
        for y, line in enumerate(initial):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    if dimensions == 3:
                        self.active[(x, y, 0)] = True
                    if dimensions == 4:
                        self.active[(x, y, 0, 0)] = True

    def _min(self):
        return tuple(min(c for c in col) for col in map(list, zip(*self.active.keys())))

    def _max(self):
        return tuple(max(c for c in col) for col in map(list, zip(*self.active.keys())))

    def _neighbours(self, coords):
        for c in itertools.product(*(range(c - 1, c + 2) for c in coords)):
            if c == coords:
                continue
            yield c

    def _extended_range(self):
        return itertools.product(*(range(mi - 1, ma + 2) for mi, ma in zip(self._min(), self._max())))

    def cycle(self):
        step = copy.deepcopy(self.active)
        # Go through all cubes "outside existing cubes" (the extended range)
        for coord in self._extended_range():
            if self.active[coord]:
                step[coord] = sum(
                    self.active[neighbour] for neighbour in self._neighbours(coord)
                ) in (2, 3)
            if not self.active[coord]:
                step[coord] = (
                    sum(self.active[neighbour] for neighbour in self._neighbours(coord))
                    == 3
                )
        self.active = step
        return self.total_active()

    def total_active(self):
        return sum(self.active.values())

    def __str__(self):
        s = ""
        mi, ma = self._min(), self._max()

        # Outer loop for the "layer printing" e.g. z=0, w=-2
        for printable in itertools.product(
            *(range(mi, ma + 1) for mi, ma in zip(mi[2:], ma[2:]))
        ):

            # Inner loop for x and y coordinates
            for y in range(mi[1], ma[1] + 1):
                for x in range(mi[0], ma[0] + 1):
                    coords = (x, y, *printable)
                    if self.active[coords]:
                        s += "#"
                    else:
                        s += "."
                s += "\n"
            s += "\n"
        return s


if __name__ == "__main__":
    initial = sys.stdin.readlines()
    print("PART 1")
    g1 = Grid(initial)
    for cycle in range(1, 7):
        print("Cycle", cycle, g1.cycle())

    print("PART 2")
    g2 = Grid(initial, dimensions=4)
    for cycle in range(1, 7):
        print("Cycle", cycle, g2.cycle())
