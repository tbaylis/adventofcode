"""
Advent of code, day 17 - Trick Shot

https://adventofcode.com/2021/day/17
"""
import fileinput
import collections

Point = collections.namedtuple("Point", ["x", "y"])


def probe_will_hit_target_area(vx, vy, xmin, xmax, ymin, ymax):
    x, y = 0, 0

    while x <= xmax and y >= ymin:
        if xmin <= x and x <= xmax and ymin <= y and y <= ymax:
            return True

        x, y = x + vx, y + vy
        vx, vy = max(0, vx - 1), vy - 1

    return False


if __name__ == "__main__":
    for line in fileinput.input():
        xr, yr = line.strip().replace("target area: ", "").split(", ")

    xmin, xmax = tuple(map(int, xr.replace("x=", "").split("..")))
    ymin, ymax = tuple(map(int, yr.replace("y=", "").split("..")))

    vx_min = min(vx for vx in range(xmax + 1) if xmin <= vx * (vx + 1) // 2 <= xmax)

    vy_max = 0
    for vy in range(ymin, abs(ymin)):
        if probe_will_hit_target_area(vx_min, vy, xmin, xmax, ymin, ymax):
            vy_max = max(vy_max, vy)
    print(f"y_max={vy_max*(vy_max+1) // 2}")

    velocities_that_hit_target = 0
    for vx in range(vx_min, xmax + 1):
        for vy in range(ymin, abs(ymin)):

            if probe_will_hit_target_area(vx, vy, xmin, xmax, ymin, ymax):
                velocities_that_hit_target += 1

    print(f"{velocities_that_hit_target=}")
