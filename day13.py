"""
Advent of code, day 13 - Shuttle Search

https://adventofcode.com/2020/day/13
"""
import fileinput


if __name__ == "__main__":
    notes = [line.strip() for line in fileinput.input()]

    departure = int(notes[0])
    idxs = notes[1].split(",")
    ids = [int(id) for id in idxs if id != "x"]
    print("departure", departure, "bus ids", ids)
    next_departures = [(departure // id + 1) * id for id in ids]
    print("next departures", next_departures)
    waiting_times = [d - departure for d in next_departures]
    print("waiting times", waiting_times)
    shortest_wait = min(waiting_times)
    bus_id = ids[waiting_times.index(min(waiting_times))]
    print(
        "part 1: min waiting time",
        shortest_wait,
        "for bus id",
        bus_id,
        "product",
        bus_id * shortest_wait,
    )

    # Part 2:
    mods = {int(id): -i % int(id) for i, id in enumerate(idxs) if id != "x"}
    values = list(reversed(sorted(mods.keys())))

    print(mods)
    t = mods[values[0]]  # First guess is the largest bus index
    r = values[0]
    print("r", r, "t", t)
    for b in values[1:]:
        while t % b != mods[b]:
            t += r
        r *= b
    print("earliest timestamp", t)
