"""
Advent of code, day 5 - Hydrothermal Venture

https://adventofcode.com/2021/day/5
"""
import fileinput
from collections import defaultdict


if __name__ == "__main__":
    orthogonal, diagonal = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for line in fileinput.input():
        x1, y1, x2, y2 = tuple(map(int, line.strip().replace(' -> ', ',').split(',')))

        if x1 == x2:
            for y in range(y1, (y2+1) if y1<y2 else (y2-1), 1 if y1<y2 else -1):
                orthogonal[(x1, y)] += 1
                diagonal[(x1, y)] += 1
        elif y1 == y2:
            for x in range(x1, (x2+1) if x1<x2 else (x2-1), 1 if x1<x2 else -1):
                orthogonal[(x, y1)] += 1
                diagonal[(x, y1)] += 1
        else:
            for x, y in zip(range(x1, (x2+1) if x1<x2 else (x2-1), 1 if x1<x2 else -1),
                            range(y1, (y2+1) if y1<y2 else (y2-1), 1 if y1<y2 else -1)):
                diagonal[(x,y)] +=1

    print(f"At least two lines overlap in the orthogonal case at {sum(r >= 2 for r in orthogonal.values())}")
    print(f"At least two lines overlap in the diagonal case at {sum(r >= 2 for r in diagonal.values())}")
