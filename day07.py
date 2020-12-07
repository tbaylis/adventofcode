"""
Advent of code, day 7 - Handy Haversacks

https://adventofcode.com/2020/day/7
"""
import fileinput
import re


if __name__ == "__main__":
    my_bag = "shiny gold"
    rules = {}
    count_colour_expression = re.compile("([\d]) ([a-z]+\W[a-z]+)")

    for line in fileinput.input():
        outer_bag, contents = line.split(" contain ")
        outer_bag = outer_bag.replace(" bags", "")

        contents = (
            contents.strip().replace(" bags", "").replace(" bag", "").replace(".", "")
        )

        if contents != "no other":
            for c in contents.split(", "):
                m = count_colour_expression.search(c)

                r = rules.get(outer_bag, {})
                r.update({m.group(2): int(m.group(1))})
                rules[outer_bag] = r
        else:
            rules[outer_bag] = {}

    def search_down(bag, rules, factor):
        colours = set()
        number = 0
        for b, c in bag.items():
            colours.add(b)
            col, num = search_down(rules[b], rules, factor * c)
            colours.update(col)
            number += num + factor * c
        return colours, number

    colours, number = search_down(rules[my_bag], rules, 1)
    print("colours", len(colours), number)
