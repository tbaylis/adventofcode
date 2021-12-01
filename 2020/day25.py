"""
Advent of code, day 25 - Combo Breaker

https://adventofcode.com/2020/day/25
"""
import sys


if __name__ == "__main__":
    data = [int(x) for x in sys.stdin.readlines()]
    i = 0
    sn = 7
    loops = {x: None for x in data}
    value = 1
    divisor = 20201227
    while any(x is None for x in loops.values()):
        value = (value * sn) % divisor
        i += 1
        if value in data:
            loops[value] = i
    sn = [k for k in loops.keys() if k != value][0]
    val = value
    value = 1
    for i in range(loops[val]):
        value = (value * sn) % divisor
    print("Part 1: {}".format(value))
