"""
Advent of code, day 7 - The Treachery of Whales

https://adventofcode.com/2021/day/7
"""
import fileinput

def linear_fuel(positions, align_to):
    return sum(abs(p-align_to) for p in positions)

def exp_fuel(positions, align_to):
    def triang(n):
        return n * (n+1) // 2
    return sum(triang(abs(p-align_to)) for p in positions)


if __name__ == "__main__":
    positions = []
    for line in fileinput.input():
        positions += map(int, line.split(','))

    p_min, p_max = min(positions), max(positions)

    min_linear_fuel = min(linear_fuel(positions, o) for o in range(p_min, p_max))
    min_exp_fuel = min(exp_fuel(positions, o) for o in range(p_min, p_max))

    print(f"{min_linear_fuel=}\n{min_exp_fuel=}")
