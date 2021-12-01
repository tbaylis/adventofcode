"""
Advent of code, day 1 - Sonar Sweep

https://adventofcode.com/2021/day/1
"""
import fileinput


if __name__ == "__main__":
    # Set the window size to 1 for the first part of the problem, and 3 for the second.
    window = [None for _ in range(3)]
    prev_window = 1e100
    window_increases = 0
    for depth in (int(line.strip()) for line in fileinput.input()):
        window.append(depth)
        window.pop(0)
        window_total = sum(window) if all(window) else 0
        if prev_window < window_total:
            print(f"{prev_window = }, {window_total = }, {window =}")
            window_increases += 1
        prev_window = window_total if all(window) else 1e100

    print(f"{window_increases = }")
