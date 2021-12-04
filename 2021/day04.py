"""
Advent of code, day 4 - Giant Squid

https://adventofcode.com/2021/day/4
"""
import fileinput

def check_bingo(board):
    for row in board:
        if all(r == None for r in row):
            return True
    for col in zip(*board):
        if all(c == None for c in col):
            return True


if __name__ == "__main__":
    draws, boards, board = [], [], []

    for line in fileinput.input():
        if fileinput.isfirstline():
            draws = map(int, line.strip().split(','))
        else:
            if line.strip() == '':
                if board != []:
                    boards.append(board)
                board = []
            else:
                board.append(list(map(int, map(str.strip, line.strip().split()))))
    boards.append(board)

    bingo_first = True
    for draw in draws:
        for board in boards:
            for row in board:
                if draw in row:
                    row[row.index(draw)] = None

        for board in boards:
            if check_bingo(board):
                board_score = sum(sum(r for r in row if r) for row in board)
                boards.remove(board)
                if bingo_first:
                    print(f"FIRST BINGO: {board_score * draw}")
                    bingo_first = False

        if len(boards) == 0:
            board_score = sum(sum(r for r in row if r) for row in board)

            print(f"LAST BINGO: {board_score * draw}")
            break
