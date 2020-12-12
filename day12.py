"""
Advent of code, day 12 - Rain Risk

https://adventofcode.com/2020/day/12
"""
import fileinput


def move(direction, step, position):
    return position[0] + step * direction[0], position[1] + step * direction[1]


def rotate(direction, dir, angle):
    if (dir == "R" and angle == 90) or (dir == "L" and angle == 270):
        return (direction[1], -direction[0])
    if (dir == "R" and angle == 180) or (dir == "L" and angle == 180):
        return (-direction[0], -direction[1])
    if (dir == "R" and angle == 270) or (dir == "L" and angle == 90):
        return (-direction[1], direction[0])


if __name__ == "__main__":
    p1, w1 = (0, 0), (1, 0)
    p2, w2 = (0, 0), (10, 1)

    for line in fileinput.input():
        dir = line.strip()[0]
        step = int(line.strip()[1:])
        print("position", p1, p2, "waypoint", w1, w2, "direction", dir, "step", step)
        if dir == "F":
            p1 = move(w1, step, p1)
            p2 = move(w2, step, p2)
            continue
        if dir == "R" or dir == "L":
            w1 = rotate(w1, dir, step)
            w2 = rotate(w2, dir, step)
            continue
        else:
            d = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}[dir]
            p1 = move(d, step, p1)
            w2 = move(d, step, w2)

    print("Problem 1", p1, "distance", abs(p1[0]) + abs(p1[1]))
    print("Problem 2", p2, "distance", abs(p2[0]) + abs(p2[1]))
