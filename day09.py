"""
Advent of code, day 9 - Encoding Error

https://adventofcode.com/2020/day/9
"""
import fileinput
import itertools



def search_by_sum_for_product(entries, total):
    for factors in entries:
        if sum(factors) == total:
            return factors


if __name__ == "__main__":
    preamble_length = 25

    numbers = []
    for line in fileinput.input():
        numbers.append(int(line.strip()))

    for index, n in enumerate(numbers):
        if index < preamble_length:
            continue
        scope = numbers[index - preamble_length : index]

        factors = search_by_sum_for_product(itertools.product(scope, scope), n)
        if factors is None:
            print("first non-sum number is", n)
            break

    # step 2
    for i in range(len(numbers)):
        for k in range(2, len(numbers[i:])):
            total = sum(numbers[i : i + k])
            if total == 90433990:
                print(
                    "encryption weakness is",
                    max(numbers[i : i + k]) + min(numbers[i : i + k]),
                )
                break
