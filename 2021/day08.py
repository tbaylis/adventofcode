"""
Advent of code, day 8 -

https://adventofcode.com/2021/day/8
"""
import fileinput


if __name__ == "__main__":
    digits_in_output_values = 0
    total_output_value = 0
    for line in fileinput.input():
        l, r = line.strip().split(" | ")
        left = list(map(set, l.split(" ")))
        left.sort(key=len)
        right = r.strip().split(" ")

        segment = {
            "A": set("abcdefg"),
            "D": set("abcdefg"),
            "G": set("abcdefg"),
            "F": set("abcdefg"),
            "B": set("abcdefg"),
            "E": set("abcdefg"),
            "C": set("abcdefg"),
        }

        # Find the 1 (length = 2)
        one = left[0]
        segment["B"] = one
        segment["C"] = one

        # Find the 7 (length 3)
        seven = left[1]
        segment["A"] = seven - one

        # all the "fives" have the three horizontal bars in common
        fives = left[3:6]
        potential_belts = fives[0].intersection(fives[1]).intersection(fives[2])

        # from the "sixes" 6 and 9, but not the 0 will have two of the potential "belts", i.e. that one will be the zero
        sixes = left[6:9]

        zero = min(sixes, key=lambda s: len(potential_belts.intersection(s)))
        segment["G"] = potential_belts - zero.intersection(potential_belts)
        segment["D"] = potential_belts - segment["A"] - segment["G"]

        # Find the 4
        four = left[2]
        segment["F"] = four - segment["G"] - segment["B"] - segment["C"]

        # Find the number five (the 'F' from the four is "on" for the five).
        the_five = list(x for x in fives if segment["F"].issubset(x))[0]

        segment["C"] = segment["C"].intersection(the_five)
        segment["B"] = segment["B"] - segment["C"]

        # Only one segment remains.
        segment["E"] = (
            segment["E"]
            - segment["A"]
            - segment["D"]
            - segment["G"]
            - segment["F"]
            - segment["B"]
            - segment["C"]
        )

        segment_mapping = {
            "".join(
                segment["B"]
                | segment["C"]
                | segment["D"]
                | segment["E"]
                | segment["F"]
                | segment["A"]
            ): "0",
            "".join(segment["B"] | segment["C"]): "1",
            "".join(
                segment["B"] | segment["E"] | segment["G"] | segment["A"] | segment["D"]
            ): "2",
            "".join(
                segment["B"] | segment["C"] | segment["G"] | segment["A"] | segment["D"]
            ): "3",
            "".join(segment["B"] | segment["C"] | segment["G"] | segment["F"]): "4",
            "".join(
                segment["F"] | segment["C"] | segment["G"] | segment["A"] | segment["D"]
            ): "5",
            "".join(
                segment["F"]
                | segment["E"]
                | segment["G"]
                | segment["A"]
                | segment["D"]
                | segment["C"]
            ): "6",
            "".join(segment["A"] | segment["B"] | segment["C"]): "7",
            "".join(
                segment["F"]
                | segment["E"]
                | segment["G"]
                | segment["A"]
                | segment["D"]
                | segment["C"]
                | segment["B"]
            ): "8",
            "".join(
                segment["F"]
                | segment["C"]
                | segment["G"]
                | segment["A"]
                | segment["D"]
                | segment["B"]
            ): "9",
        }

        digits = ""
        for num in right:
            for key, val in segment_mapping.items():
                if set(key) == set(num):
                    digits += val

        total_output_value += int(digits)
        digits_in_output_values += sum(1 for r in right if len(r) in (2, 3, 4, 7))

    print(f"{digits_in_output_values=}")
    print(f"{total_output_value=}")
