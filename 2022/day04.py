"""
Advent of code, day 4 - Camp Cleanup

https://adventofcode.com/2022/day/4
"""
import fileinput


if __name__ == "__main__":
    fully_overlapping = 0
    overlapping = 0

    for line in fileinput.input():
        p1, p2 = line.strip().split(',')
        i1 = set(range(int(p1.split('-')[0]), int(p1.split('-')[1])+1))
        i2 = set(range(int(p2.split('-')[0]), int(p2.split('-')[1])+1))
        if len(i1.intersection(i2)) > 0 and (i1.intersection(i2) == i1 or i1.intersection(i2) == i2):
            fully_overlapping += 1
        if len(i1.intersection(i2)):
            overlapping += 1

    print(f"Part 1: {fully_overlapping}")
    print(f"Part 2: {overlapping}")
