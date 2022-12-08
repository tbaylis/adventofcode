"""
Advent of code, day 3 - Rucksack Reorganization

https://adventofcode.com/2022/day/3
"""
import fileinput

def prioritise(symbol):
    if symbol > 'a':
        return ord(symbol) - 96
    return ord(symbol) - 38

if __name__ == "__main__":
    total_priority, group_priority = 0, 0
    groups = set()

    for i, rucksack in enumerate(fileinput.input()):
        first = rucksack.strip()[0:(len(rucksack.strip()) // 2)]
        second = rucksack.strip()[(len(rucksack.strip()) // 2):]

        shared = list(set(first).intersection(set(second)))[0]
        priority = prioritise(shared)

        total_priority += priority
        
        if i % 3 == 0:
            groups = set(rucksack.strip())
        groups = groups.intersection(set(rucksack.strip()))
        if (i + 1) % 3 == 0:
            group_priority += prioritise(list(groups)[0])

        
    print(f"Part 1: {total_priority}")
    print(f"Part 2: {group_priority}")
