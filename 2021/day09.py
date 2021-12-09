"""
Advent of code, day 9 - Smoke Basin

https://adventofcode.com/2021/day/9
"""
import fileinput
import functools
import operator


def flood_fill(seed, grid):
    queue = [seed]

    basin_size = 0
    while queue:
        n = queue.pop(0)
        if grid.get(n, 10) < 9:
            grid[n] = 9
            basin_size += 1
            queue.append((n[0], n[1] - 1))
            queue.append((n[0], n[1] + 1))
            queue.append((n[0] - 1, n[1]))
            queue.append((n[0] + 1, n[1]))
    return basin_size


def find_basins(grid):
    low_points = []
    for p in grid.keys():

        if all(
            grid[p] < grid.get(n, 10)
            for n in (
                (p[0], p[1] - 1),
                (p[0], p[1] + 1),
                (p[0] - 1, p[1]),
                (p[0] + 1, p[1]),
            )
        ):
            low_points.append(p)
    return low_points


if __name__ == "__main__":
    grid = {}
    for row_index, line in enumerate(fileinput.input()):
        for col_index, chr in enumerate(line.strip()):
            grid[(row_index, col_index)] = int(chr)

    basins = find_basins(grid)

    total_risk_level = sum(grid[point] + 1 for point in basins)

    basin_sizes = [flood_fill(lp, grid) for lp in basins]
    basin_sizes.sort()
    product_of_three_largest_basins = functools.reduce(
        operator.mul, basin_sizes[-3:], 1
    )

    print(f"{total_risk_level=}")
    print(f"{product_of_three_largest_basins=}", basin_sizes[-3:])
