"""
Advent of code, day 18 - Operation Order

https://adventofcode.com/2020/day/18
"""
import fileinput
import math
import copy


def evaluate_basic(stmt):
    total = 0
    operator = sum
    while stmt:
        element = stmt.pop(0)
        if element == "(":
            total = operator((total, evaluate_basic(stmt)))
        elif element == ")":
            return total
        elif element == "+":
            operator = sum
        elif element == "*":
            operator = math.prod
        else:
            total = operator((total, int(element)))
    else:
        return total


def evaluate_advanced(stmt):
    output = []
    ops = []

    while stmt:
        token = stmt.pop(0)
        if isinstance(token, int):
            output.append(token)
        elif token in ("+", "*"):
            while ops and token == "*" and ops[-1] == "+":
                output.append(ops.pop())
            ops.append(token)
        elif token == "(":
            ops.append(token)
        elif token == ")":
            while ops and ops[-1] != "(":
                output.append(ops.pop())
            if ops[-1] == "(":
                ops.pop()
    while ops:
        output.append(ops.pop())

    return eval_polish_notation(output)


def eval_polish_notation(stmt):
    stack = []
    for token in stmt:
        # print("token", token)
        if token not in ["+", "*"]:
            stack.append(token)
        elif token == "+":
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(stack.pop() * stack.pop())
    return stack[0]


if __name__ == "__main__":
    assert evaluate_basic([2, "*", 3, "+", "(", 4, "*", 5, ")"]) == 26
    assert evaluate_basic([1, "+", 2, "*", 3, "+", 4, "*", 5, "+", 6]) == 71
    assert evaluate_advanced([2, "*", 3, "+", "(", 4, "*", 5, ")"]) == 46

    homework_basic = 0
    homework_advanced = 0
    for line in fileinput.input():
        stmt = []
        for c in [c for c in line.strip() if c != " "]:
            if c.isdigit():
                stmt.append(int(c))
            else:
                stmt.append(c)

        homework_basic += evaluate_basic(copy.deepcopy(stmt))
        homework_advanced += evaluate_advanced(stmt)
    print("homework basic", homework_basic, "homework advanced", homework_advanced)
