"""
Advent of code, day 5 - Binary Boarding

https://adventofcode.com/2020/day/5
"""
import fileinput

if __name__ == "__main__":
    seat_ids = set()

    for line in fileinput.input():
        row = int(line[:7].replace("B", "1").replace("F", "0"), 2)
        column = int(line[-4:].strip().replace("R", "1").replace("L", "0"), 2)

        seat_id = row * 8 + column
        # print(line.strip(), 'row', row, 'column', column, 'seat ID', seat_id)
        seat_ids.add(seat_id)

    print("max seat ID", max(seat_ids))

    all_seats = set(range(min(seat_ids), max(seat_ids)))
    print("empty seat ID", all_seats.difference(seat_ids))
