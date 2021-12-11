"""
Advent of code, day 11 - Dumbo Octopus

https://adventofcode.com/2021/day/11
"""
import fileinput


if __name__ == "__main__":

    grid = {}
    for row_index, line in enumerate(fileinput.input()):
        for col_index, chr in enumerate(line.strip()):
            grid[(row_index, col_index)] = int(chr)

    total_flashes = 0
    for iteration in range(1, 217):
        flashed = set()
        flashes = []
        for p in grid.keys():
            grid[p] += 1
            if grid[p] > 9:
                flashes.append(p)

        while flashes:
            p = flashes.pop(0)
            flashed.add(p)
            for n in [(p[0], p[1] - 1), (p[0], p[1] + 1), (p[0] - 1, p[1]), (p[0] + 1, p[1]),
                        (p[0] + 1, p[1] -1), (p[0] + 1, p[1] +1), (p[0] - 1, p[1] -1), (p[0] - 1, p[1] +1)]:
                if n in grid.keys() and n not in flashed and n not in flashes:
                    grid[n] += 1
                    if grid[n] > 9:
                        flashes.append(n)

        for p,v in grid.items():
            if v > 9:
                grid[p] = 0
                total_flashes += 1
        if len(flashed) == 100:
            print(f"All octopi flashed simultaneously at iteration {iteration}")

        if iteration == 10:
            print(f"{total_flashes=}, 204")
        if iteration == 100:
            print(f"{total_flashes=}, 1656")
