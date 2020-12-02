"""
Advent of code, day 2 - Password Philosophy

https://adventofcode.com/2020/day/2
"""
import fileinput

if __name__ == "__main__":
    sled_policy = 0
    toboggan_policy = 0

    for policy_with_password in fileinput.input():
        # Parse line (policy_with_password) like "3-11 k: password"
        rule, pw = policy_with_password.split(": ", maxsplit=1)
        minmax, symbol = rule.split(" ", maxsplit=1)
        lower, upper = (int(x) for x in minmax.split("-", maxsplit=1))

        # Count number of occurrences of symbol in pw
        num_symbols = pw.count(symbol)

        if (lower <= num_symbols) and (num_symbols <= upper):
            sled_policy += 1

        # Check that the character at lower is the same as symbol or that the character
        # at upper is the same as symbol, note that not both are allowed (thus the
        # "exclusive or" ^).
        if (pw[lower - 1] is symbol) ^ (pw[upper - 1] is symbol):
            toboggan_policy += 1

    print(f"Sled password policy matches {sled_policy} = 655")
    print(f"Toboggan password policy matches {toboggan_policy} = 673")
