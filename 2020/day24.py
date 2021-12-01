"""
Advent of code, day 24 - Lobby Layout

https://adventofcode.com/2020/day/24
"""
import sys
import collections

directions = {
    "se": 0.5 - 1j,
    "e": 1,
    "w": -1,
    "ne": 0.5 + 1j,
    "sw": -0.5 - 1j,
    "nw": -0.5 + 1j,
}


def parse(lines):
    inputs = []
    for line in lines:
        l = collections.deque(line.strip())
        tiles = []
        while l:
            d = l.popleft()
            if d in {"s", "n"}:
                d += l.popleft()
            tiles.append(directions[d])
        inputs.append(tiles)
    return inputs


def get_adj_tiles(t):
    return {t - 1, t + 1, t + 0.5 - 1j, t + 0.5 + 1j, t - 0.5 + 1j, t - 0.5 - 1j}


def black_tiles_after_100_days(blacks):
    for i in range(1, 101):
        new_black_tiles = set()

        for t in blacks:
            adj = get_adj_tiles(t)
            adj_black_tiles = len(adj & blacks)

            if 0 < adj_black_tiles < 3:
                new_black_tiles.add(t)

            for ad in adj:
                if ad in blacks:
                    continue
                new_adj = get_adj_tiles(ad)
                if len(new_adj & blacks) == 2:
                    new_black_tiles.add(ad)
        blacks = new_black_tiles
    return len(blacks)


if __name__ == "__main__":
    inputs = parse(sys.stdin.readlines())
    flips = collections.defaultdict(int)
    for d in inputs:
        pos = sum(d)
        flips[pos] += 1
    blacks = {k for k, v in flips.items() if v % 2 == 1}
    print("Part 1:", len(blacks))

    print("Part 2:", black_tiles_after_100_days(blacks))
