"""
Advent of code, day 23 - Crab Cups

https://adventofcode.com/2020/day/23
"""
import sys


def play_game(start, links, rounds):
    N = len(links) - 1
    current = start
    pick = [0, 0, 0]
    dest = 0
    for _ in range(rounds):
        n = links[current]
        for i in range(3):
            pick[i], n = n, links[n]
        dest = ((current - 2) % N) + 1
        while dest in pick:
            dest = ((dest - 2) % N) + 1
        links[current], links[pick[2]], links[dest] = (
            links[pick[2]],
            links[dest],
            pick[0],
        )
        current = links[current]
    return links


if __name__ == "__main__":
    lines = sys.stdin.readline()
    cups = [int(c) for c in lines.strip()]
    N = len(cups)

    links = [0 for _ in range(N + 1)]
    for i, n in enumerate(cups):
        links[n] = cups[(i + 1) % N]

    links = play_game(start=cups[0], links=links, rounds=100)

    lst = [0 for _ in range(N + 1)]
    n = 1
    for i in range(n, N + 1):
        lst[i] = n
        n = links[n]

    print("Part 1:", "".join(str(n) for n in lst[2:]))

    # Part 2
    N2 = 1000000
    links = list(0 for _ in range(N2 + 1))

    for i, n in enumerate(cups):
        links[n] = cups[(i + 1) % N]
    for n in range(N + 1, N2):
        links[n] = n + 1
    links[cups[-1]] = N + 1
    links[N2] = cups[0]

    play_game(cups[0], links, 10000000)
    val2 = links[1]
    val2 *= links[val2]

    print("Part 2:", val2)
