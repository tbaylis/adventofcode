"""
Advent of code, day 1 - Calorie Counting

https://adventofcode.com/2022/day/1
"""
from collections import defaultdict
import fileinput


if __name__ == "__main__":
    calories = [0]

    for line in fileinput.input():
        if line.strip() == "":
            calories.append(0)
            continue

        calories[-1] += int(line.strip())

    print(f"Part 1: {max(calories)}")
    print(f"Part 2: {sum(sorted(calories)[-3:])}")
