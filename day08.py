"""
Advent of code, day 8 - Handheld Halting

https://adventofcode.com/2020/day/8
"""
import fileinput
import copy


def run_instructions(instructions):
    acc = 0
    pos = 0
    used_instructions = set()

    while True:
        # print('pos', pos, 'len', len(instructions), instructions[pos])
        used_instructions.add(pos)

        if instructions[pos][0] == "nop":
            pos += 1

        elif instructions[pos][0] == "jmp":
            pos += instructions[pos][1]

        elif instructions[pos][0] == "acc":
            acc += instructions[pos][1]
            pos += 1

        if (pos in used_instructions) or (pos == len(instructions)):
            break

    return acc, pos != len(instructions)


if __name__ == "__main__":
    instructions = []

    for line in fileinput.input():
        op, arg = line.strip().split(" ")
        instructions.append((op, int(arg)))

    # Start interpreting
    acc, looped = run_instructions(instructions)

    print("first accumulator", acc, "infinite loop", looped)

    # Try perturbation
    p_instr = 0
    while p_instr < len(instructions):
        perturbed = copy.deepcopy(instructions)
        if perturbed[p_instr][0] == "jmp":
            perturbed[p_instr] = ("nop", perturbed[p_instr][1])
            p_instr += 1
        elif perturbed[p_instr][0] == "nop":
            perturbed[p_instr] = ("jmp", perturbed[p_instr][1])
            p_instr += 1
        else:
            p_instr += 1
            continue

        acc, looped = run_instructions(perturbed)

        if not looped:
            # Working perturbed
            break

    print("second accumulator", acc, "infinite loop", looped)
