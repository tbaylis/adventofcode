"""
Advent of code, day 10 - Adapter Array

https://adventofcode.com/2020/day/10
"""
import fileinput


def arrangements(joltages):
    next_steps = {
        jolt: [j for j in joltages[i + 1 : i + 4] if j - jolt <= 3]
        for i, jolt in enumerate(joltages[:-1])
    }

    arrangements = {joltages[-1]: 1}
    for joltage in reversed(joltages[:-1]):
        arrangements[joltage] = sum(arrangements[j] for j in next_steps[joltage])

    return arrangements[0]


if __name__ == "__main__":
    joltages = [0]
    hist = {1: 0, 2: 0, 3: 0}
    for line in fileinput.input():
        joltages.append(int(line.strip()))

    joltages = sorted(joltages)
    joltages.append(joltages[-1] + 3)
    diffs = (abs(j1 - j2) for j1, j2 in zip(joltages, joltages[1:]))
    for d in diffs:
        hist[d] += 1

    print("product is", hist[1] * hist[3], "histogram", hist)
    print("number of arrangements", arrangements(joltages))
