"""
Advent of code, day 13 - Passage Pathing

https://adventofcode.com/2021/day/13
"""
import fileinput

def disp(ps):
    xs, ys = max(p[0] for p in ps), max(p[1] for p in ps)
    display = [["."] * (xs + 1) for _ in range(ys + 1)]

    for x, y in ps:
        display[y][x] = "#"

    print("\n".join("".join(row) for row in display))


if __name__ == "__main__":
    points, folds = [], []
    for line in fileinput.input():
        if ',' in line:
            points.append(tuple(map(int, line.strip().split(','))))
        if '=' in line:
            dir, val = line.strip().replace('fold along ', '').split('=')
            folds.append((dir, int(val)))

    for fold_count, (fold_dir, val) in enumerate(folds):
        np = set()
        if fold_dir == 'y':
            for point in points:
                if point[1] < val:
                    np.add(point)
                elif point[1] > val:
                    np.add((point[0], 2 * val - point[1]))
        else:
            for point in points:
                if point[0] < val:
                    np.add(point)
                elif point[0] > val:
                    np.add((2 * val - point[0], point[1]))
        points = list(np)

        if fold_count == 0:
            print(f"points={len(points)} after one fold")

    disp(points)
