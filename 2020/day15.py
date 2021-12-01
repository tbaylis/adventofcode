"""
Advent of code, day 15 - Rambunctious Recitation

https://adventofcode.com/2020/day/15
"""
import fileinput
import copy


def produce_numbers(numbers, steps=2020):
    spoken_numbers = {n: (i,) for i, n in enumerate(numbers)}
    last_spoken = numbers[-1]

    for i in range(len(numbers), steps):
        indices = spoken_numbers.get(last_spoken)

        next_number = 0
        if len(indices) == 2:
            next_number = indices[0] - indices[1]

        indices = spoken_numbers.get(next_number, (i,))
        spoken_numbers[next_number] = (i, indices[0])

        last_spoken = next_number
    return last_spoken


if __name__ == "__main__":
    numbers = []
    for line in fileinput.input():
        numbers += (int(c) for c in line.strip().split(","))

    print("[0, 3, 6] ->", produce_numbers([0, 3, 6], steps=10), "= 0")
    print("[0, 3, 6] ->", produce_numbers([0, 3, 6]), "= 436")
    print("[1, 3, 2] ->", produce_numbers([1, 3, 2]), "= 1")
    print("[2, 1, 3] ->", produce_numbers([2, 1, 3]), "= 10")
    print("[1, 2, 3] ->", produce_numbers([1, 2, 3]), "= 27")
    print("[2, 3, 1] ->", produce_numbers([2, 3, 1]), "= 78")
    print("[3, 2, 1] ->", produce_numbers([3, 2, 1]), "= 438")
    print("[3, 1, 2] ->", produce_numbers([3, 1, 2]), "= 1836")

    print(numbers, "->", produce_numbers(copy.deepcopy(numbers), steps=2020))

    print("[0, 3, 6] ->", produce_numbers([0, 3, 6], steps=30000000), "= 175594")
    print("[1, 3, 2] ->", produce_numbers([1, 3, 2], steps=30000000), "= 2578")
    print("[2, 1, 3] ->", produce_numbers([2, 1, 3], steps=30000000), "= 3544142")
    print("[1, 2, 3] ->", produce_numbers([1, 2, 3], steps=30000000), "= 261214")
    print("[2, 3, 1] ->", produce_numbers([2, 3, 1], steps=30000000), "= 6895259")
    print("[3, 2, 1] ->", produce_numbers([3, 2, 1], steps=30000000), "= 18")
    print("[3, 1, 2] ->", produce_numbers([3, 1, 2], steps=30000000), "= 362")

    print(numbers, "->", produce_numbers(copy.deepcopy(numbers), steps=30000000))
