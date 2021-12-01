"""
Advent of code, day 1 - Report repair

https://adventofcode.com/2020/day/1
"""
import itertools
import functools
import operator
import fileinput


def search_by_sum_for_product(entries, total=2020):
    for factors in entries:
        if sum(factors) == total:
            product = functools.reduce(operator.mul, factors, 1)
            print(f"Sum of {factors} is {total} and product is {product}")
            break


if __name__ == "__main__":
    expenses = []
    for line in fileinput.input():
        expenses.append(int(line.strip()))

    search_by_sum_for_product(itertools.product(expenses, expenses))

    search_by_sum_for_product(itertools.product(expenses, expenses, expenses))
