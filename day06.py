"""
Advent of code, day 6 - Custom Customs

https://adventofcode.com/2020/day/6
"""
import fileinput

if __name__ == "__main__":
    groups_any, groups_all = [], []
    group_any, group_all = None, None

    for line in fileinput.input():
        if line == "\n":
            groups_any.append(group_any)
            groups_all.append(group_all)
            group_any = None
            group_all = None

        else:
            person = set(char for char in line.strip())
            if group_any is None or group_all is None:
                group_any = person
                group_all = person
            group_any = group_any.union(person)
            group_all = group_all.intersection(person)

    groups_any.append(group_any)
    groups_all.append(group_all)

    print("any", groups_any, "all", groups_all)
    print("groups_any", sum(len(g) for g in groups_any))
    print("groups_all", sum(len(g) for g in groups_all))
