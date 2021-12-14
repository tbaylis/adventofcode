"""
Advent of code, day 14 - Extended Polymerization

https://adventofcode.com/2021/day/14
"""
import fileinput
import collections


def polymerise(insertions, polymer, N):
    poly_pairs = collections.Counter("".join(p) for p in zip(polymer, polymer[1:]))

    for _ in range(1, N + 1):
        new_pairs = collections.defaultdict(int)
        for (l, r), cnt in poly_pairs.items():
            p1, p2 = l + insertions[l][r], insertions[l][r] + r
            new_pairs[p1] += cnt
            new_pairs[p2] += cnt
        poly_pairs = {k: v for k, v in new_pairs.items()}

    d = collections.defaultdict(int)
    for p, cnt in poly_pairs.items():
        d[p[0]] += cnt
    d[polymer[-1]] += 1

    return max(d.values()) - min(d.values())


if __name__ == "__main__":
    polymer = ""
    insertions = collections.defaultdict(dict)
    for line in fileinput.input():
        if fileinput.isfirstline():
            polymer = line.strip()
        elif line.strip() == "":
            continue
        else:
            ins, c = line.strip().split(" -> ")
            insertions[ins[0]][ins[1]] = c

    print(f"Template:     {polymer}")
    p1 = polymerise(insertions, polymer, 10)
    p2 = polymerise(insertions, polymer, 40)
    print(f"{p1=}, {p2=}")
