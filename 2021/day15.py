"""
Advent of code, day 15 - Chiton

https://adventofcode.com/2021/day/15
"""
import fileinput

def djikstra(grid, start):
    unvisited = {n: None for n in grid.keys()}
    visited = {}
    max_col = max(x for x,_ in grid.keys())
    max_row = max(y for _,y in grid.keys())

    p = start
    current_risk = 0
    unvisited[p] = current_risk

    while True:
        for neighbour in (set([(min(p[0]+1, max_col), p[1]), (max(p[0]-1, 0), p[1]), (p[0], min(p[1]+1, max_row)), (p[0], max(p[1]-1, 0))]) - set([p])):
            if neighbour not in unvisited:
                continue

            new_risk = current_risk + grid[neighbour]

            if unvisited[neighbour] is None or unvisited[neighbour] > new_risk:
                unvisited[neighbour] = new_risk
        visited[p] = current_risk
        del unvisited[p]
        if not unvisited:
            break

        candidates = [n for n in unvisited.items() if n[1]]
        p, current_risk = sorted(candidates, key=lambda n: n[1])[0]
    return visited


if __name__ == "__main__":
    input = {}
    for row, line in enumerate(fileinput.input()):
        for col, score in enumerate(line.strip()):
            input[(int(col), int(row))] = int(score)
    print(f"len(input)={len(input)}")

    grid = {}
    grid_copies = 5
    X = max(x for x,_ in input.keys()) + 1
    Y = max(y for _,y in input.keys()) + 1
    for p, v in input.items():
        for r in range(0, grid_copies):
            for c in range(0, grid_copies):
                grid[p[0] + X * r, p[1] + Y*c] = (v + r + c - 1) % 9 +1

    top_left = (0,0)
    bottom_right = (max(x for x,_ in grid.keys()), max(y for _,y in grid.keys()))
    visited = djikstra(grid, top_left)

    print(f"risk={visited[bottom_right]}")
