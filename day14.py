"""
Advent of code, day 14 - Docking Data

https://adventofcode.com/2020/day/14
"""
import fileinput
import copy
import itertools


def value_decoder(mask, value):
    value = "{0:036b}".format(value)
    assert len(mask) == len(value)
    result = ""
    for i, m in enumerate(mask):
        if m == "X":
            result += value[i]
        if m == "1":
            result += "1"
        if m == "0":
            result += "0"
    return int(result, base=2)


def memory_address_decoder(mask, address):
    address = "{0:036b}".format(address)
    assert len(mask) == len(address)
    result = []
    number_of_x = 0
    for i, m in enumerate(mask):
        if m == "1":
            result.append("1")
        elif m == "X":
            result.append("X")
            number_of_x += 1
        else:
            result.append(address[i])

    results = [copy.deepcopy(result) for _ in range(2 ** number_of_x)]

    for i, tuple in enumerate(itertools.product((0, 1), repeat=number_of_x)):
        for t in tuple:
            for k, _ in enumerate(results[i]):
                if results[i][k] == "X":
                    results[i][k] = str(t)
                    break

    return [int("".join(r), base=2) for r in results]


if __name__ == "__main__":
    mem1 = {}
    mem2 = {}
    mask = ""
    for line in fileinput.input():
        if line.startswith("mask"):
            mask = line.strip().split(" = ")[1]
            continue

        address, v = line.strip().split(" = ", maxsplit=1)
        value = int(v)
        address = int(address.replace("mem[", "").replace("]", ""))

        mem1[address] = value_decoder(mask, value)

        addresses = memory_address_decoder(mask, address)
        for address in addresses:
            mem2[address] = value

    print("memory sum 1:", sum(mem1.values()))
    print("memory sum 2:", sum(mem2.values()))
