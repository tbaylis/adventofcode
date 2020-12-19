"""
Advent of code, day 19 - Monster Messages

https://adventofcode.com/2020/day/19
"""
import sys


def test(message, rules, r=0):
    if rules[r][0]:  # Current r points to a leaf value ("a" or "b")
        return set([1]) if (message and message[0] == rules[r][0]) else set()
    else:
        # r points to a list of sub-rules
        all_matches = set()
        for sub in rules[r][1]:
            sub_match = set([0])
            for rule in sub:
                new_match = set()
                for n in sub_match:
                    new_match |= {n + m for m in test(message[n:], rules, rule)}
                sub_match = new_match
            all_matches |= sub_match
        return all_matches


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    rule_lines = lines[: lines.index("\n")]
    message_lines = lines[lines.index("\n") :]
    rules = {}
    for i, r in (l.strip().split(": ") for l in rule_lines):
        if "a" in r or "b" in r:
            rules[int(i)] = (r[1], None)
        else:
            rs = [[int(n) for n in c.split()] for c in r.split("|")]
            rules[int(i)] = (None, rs)

    messages = [l.strip() for l in message_lines]
    print("part 1:", sum(len(m) in test(m, rules) for m in messages))

    # Update the rules so that loops are possible
    rules[8] = (None, [[42], [42, 8]])
    rules[11] = (None, [[42, 31], [42, 11, 31]])

    print("part 2:", sum(len(m) in test(m, rules) for m in messages))
