"""
Advent of code, day 3 - Binary Diagnostic

https://adventofcode.com/2021/day/3
"""
import sys
from collections import Counter

if __name__ == "__main__":
    gamma, epsilon = '', ''
    input_lines = list(map(str.strip, sys.stdin.readlines()))
    for column in zip(*input_lines):
        c = Counter(column).most_common()
        gamma += c[0][0]
        epsilon += c[-1][0]
    gamma_dec, epsilon_dec = int(gamma, base=2), int(epsilon, base=2)
    print(f"{gamma = } {gamma_dec = }, {epsilon = } {epsilon_dec = }, product = {epsilon_dec * gamma_dec}")

    o2 = input_lines[:]
    co2 = input_lines[:]
    bit = 0
    while len(o2) > 1:
        common = Counter([n[bit] for n in o2]).most_common()
        if len(common) == 1:
            keep = common[0][0]
        else:
            keep = '1' if common[0][1] == common[1][1] else common[0][0]
        o2 = [n for n in o2 if n[bit] == keep]
        bit += 1

    bit = 0
    while len(co2) > 1:
        common = Counter([n[bit] for n in co2]).most_common()
        keep = '0' if common[0][1] == common[1][1] else common[-1][0][0]
        co2 = [n for n in co2 if n[bit] == keep]
        bit += 1

    print(f"{bit=}, {o2=}, O2: {int(o2[0], base=2)}")
    print(f"{bit=}, {co2=}, CO2: {int(co2[0], base=2)}")
    print(f"{int(co2[0], base=2)} * {int(o2[0], base=2)} = {int(o2[0], base=2)*int(co2[0], base=2)}")
