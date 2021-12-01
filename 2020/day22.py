"""
Advent of code, day 22 - Crab Combat

https://adventofcode.com/2020/day/22
"""
import sys


def play(decks):
    while min(len(v) for v in decks.values()):
        c1 = decks["Player 1"].pop(0)
        c2 = decks["Player 2"].pop(0)
        if c1 > c2:
            decks["Player 1"] += [c1, c2]
        else:
            decks["Player 2"] += [c2, c1]
    return decks


def play_recursive(decks):
    old_hands = set()
    while min(len(v) for v in decks.values()):
        p1 = ",".join(str(c) for c in decks["Player 1"])
        p2 = ",".join(str(c) for c in decks["Player 2"])
        if (p1, p2) in old_hands:
            # End game, player 1 wins
            return 0, decks["Player 1"]
        old_hands.add((p1, p2))
        c1 = decks["Player 1"].pop(0)
        c2 = decks["Player 2"].pop(0)

        if c1 <= len(decks["Player 1"]) and c2 <= len(decks["Player 2"]):
            winner = play_recursive(
                {"Player 1": decks["Player 1"][:c1], "Player 2": decks["Player 2"][:c2]}
            )[0]
            if winner == 0:
                decks["Player 1"] += [c1, c2]
            else:
                decks["Player 2"] += [c2, c1]
        else:
            # Normal game
            if c1 > c2:
                decks["Player 1"] += [c1, c2]
            else:
                decks["Player 2"] += [c2, c1]
    return (
        (0, decks["Player 1"]) if len(decks["Player 1"]) > 0 else (1, decks["Player 2"])
    )


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    decks = {
        d[0].strip().replace(":", ""): [int(c) for c in d[1:]]
        for d in [lines[: lines.index("\n")], lines[lines.index("\n") + 1 :]]
    }

    decks = play(decks)

    print(
        "Part 1: score",
        sum(
            sum((i + 1) * v for i, v in enumerate(reversed(pv)))
            for pv in decks.values()
        ),
    )

    # Reset decks for part 2:
    decks = {
        d[0].strip().replace(":", ""): [int(c) for c in d[1:]]
        for d in [lines[: lines.index("\n")], lines[lines.index("\n") + 1 :]]
    }
    _, decks = play_recursive(decks)
    print("Part 2: score", sum((i + 1) * v for i, v in enumerate(reversed(decks))))
