"""
Advent of code, day 3 - The toboggan trajectory

https://adventofcode.com/2020/day/3
"""
import fileinput
import copy


if __name__ == "__main__":
    orig_slope = []
    for line in fileinput.input():
        orig_slope.append([char for char in line.strip()])

    # print('\n'.join(''.join(s) for s in orig_slope))

    for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        slope = copy.deepcopy(orig_slope)

        x, y, number_of_trees = 0, 0, 0

        while y < len(slope):
            if slope[y][x] == "#":  # tree!
                number_of_trees += 1
                slope[y][x] = "X"
            else:
                slope[y][x] = "O"

            y, x = y + dy, (x + dx) % (len(slope[0]))

        # print('\n'.join(''.join(s) for s in slope))
        print(f"Hit {number_of_trees} trees on the way down for ({dx},{dy})")
