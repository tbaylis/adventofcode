"""
Advent of code, day 16 - Ticket Translation

https://adventofcode.com/2020/day/16
"""
import fileinput
import math
import collections


def simple_ticket_validator(ticket, criteria):
    invalid = []

    is_valid = True
    for t in ticket:
        valid = any(t in r for r in rules.values())
        if not valid:
            invalid.append(t)
        is_valid = is_valid and valid

    return is_valid, invalid


if __name__ == "__main__":
    rules = {}
    my_ticket = []
    nearby_tickets = []

    reader = fileinput.input()
    line = reader.readline()
    while line != "\n":
        l = line.strip()
        name, criteria = l.split(": ")
        c1, c2 = criteria.split(" or ")
        l1, u1 = c1.split("-")
        l2, u2 = c2.split("-")
        rules[name] = list(range(int(l1), int(u1) + 1)) + list(
            range(int(l2), int(u2) + 1)
        )

        line = reader.readline()

    line = reader.readline()
    while line != "\n":
        l = line.strip()
        if l != "your ticket:":
            my_ticket = [int(c) for c in l.split(",")]

        line = reader.readline()

    line = reader.readline()
    while line != "\n" and line != "":
        l = line.strip()
        if l != "nearby tickets:":
            nearby_tickets.append([int(c) for c in l.split(",")])
        line = reader.readline()

    invalid_values = []
    valid_tickets = []
    for ticket in nearby_tickets:
        is_valid, values = simple_ticket_validator(ticket, rules.values())
        if not is_valid:
            invalid_values.append(*values)
        else:
            valid_tickets.append(ticket)

    print("sum of invalid values", sum(invalid_values))

    transposed_valid_tickets = list(map(list, zip(*valid_tickets)))

    possible = collections.defaultdict(set)
    for index in range(len(rules)):
        for field, scope in rules.items():
            if all(ticket[index] in scope for ticket in valid_tickets):
                possible[field].add(index)

    official = dict()
    departures = 1

    actual_ticket = {}
    for field in sorted(possible, key=lambda i: len(possible[i])):
        for index in possible[field]:
            if index not in official.values():
                official[field] = index
                actual_ticket[field] = my_ticket[index]
                if field.startswith("departure"):
                    departures = departures * my_ticket[index]

    print(
        "product of departure prefixed values",
        math.prod([v for k, v in actual_ticket.items() if k.startswith("departure")]),
    )
