"""
Advent of code, day 2 - Dive!

https://adventofcode.com/2021/day/2
"""
import fileinput

def read_commands():
    for line in fileinput.input():
        dir, dist = line.strip().split(' ')
        yield (dir, int(dist))


if __name__ == "__main__":
    part_one = {'depth': 0, 'horiz': 0}
    part_two = {'depth': 0, 'horiz': 0, 'aim': 0}

    for dir, dist in read_commands():
        if dir == 'forward':
            part_one['horiz'] += dist
            part_two['horiz'] += dist
            part_two['depth'] += part_two['aim'] * dist

        elif dir == 'down':
            part_one['depth'] += dist
            part_two['aim'] += dist

        elif dir == 'up':
            part_one['depth'] -= dist
            part_two['aim'] -= dist

        print(f"{dir} {dist} => {part_one = }, {part_two = }")
    print(f"End product of part 1: {part_one['horiz']} * {part_one['depth']} = {part_one['horiz']*part_one['depth']}")
    print(f"End product of part 2: {part_two['horiz']} * {part_two['depth']} = {part_two['horiz']*part_two['depth']}")
