"""
Advent of code, day 10 - Syntax Scoring

https://adventofcode.com/2021/day/10
"""
import fileinput

ILLEGAL_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_SCORES = {")": 1, "]": 2, "}": 3, ">": 4}
PAIRS = {"(": ")", "[": "]", "{": "}", "<": ">"}

if __name__ == "__main__":
    total_score = 0
    autocomplete_scores = []

    for line in fileinput.input():
        delimiters = list(line.strip())

        stack = []
        corrupt = False
        while len(delimiters) > 0 and not corrupt:
            delimiter = delimiters.pop(0)

            if delimiter in PAIRS.keys():
                stack.append(delimiter)

            elif delimiter in PAIRS.values():
                start = stack.pop()
                if PAIRS[start] != delimiter:
                    total_score += ILLEGAL_SCORE[delimiter]
                    corrupt = True

        if corrupt:
            continue

        autocomplete_score = 0
        while stack:
            delimiter = stack.pop()
            autocomplete_score = (
                5 * autocomplete_score + AUTOCOMPLETE_SCORES[PAIRS[delimiter]]
            )

        autocomplete_scores.append(autocomplete_score)

    autocomplete_scores.sort()
    print(
        f"{total_score=}, median autocomple_score={autocomplete_scores[len(autocomplete_scores) // 2]}"
    )
