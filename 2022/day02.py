"""
Advent of code, day 2 - Rock Paper Scissors

https://adventofcode.com/2022/day/2
"""
from collections import defaultdict
import fileinput

shape_score = {'X': 1, 'Y': 2, 'Z': 3}
win_score = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}
tactic = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'},
}

if __name__ == "__main__":
    score1, score2 = 0, 0

    for line in fileinput.input():
        opponent, player = line.strip().split(' ')[:2]
        score1 +=  win_score[opponent][player] + shape_score[player]

        player2 = tactic[opponent][player]
        score2 += win_score[opponent][player2] + shape_score[player2]

    print(f"Part 1: {score1}")
    print(f"Part 2: {score2}")
