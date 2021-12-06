"""
Advent of code, day 6 - Lanternfish

https://adventofcode.com/2021/day/6
"""
import fileinput

if __name__ == "__main__":
    state = [0 for _ in range(9)]
    for line in fileinput.input():
        for f in line.strip().split(','):
            state[int(f)] += 1

    print(f"Initial state: {state}, total fish: {sum(state)}")

    for day in range(1, 257):
        popped = state.pop(0)
        state.append(popped)
        state[6] += popped
        if day == 18 or day == 80 or day == 256:
            print(f"After {day} days: {state}, total fish: {sum(state)}")
