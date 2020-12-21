"""
Advent of code, day 21 - Allergen Assessment

https://adventofcode.com/2020/day/21
"""
import sys
import re
import collections

Recipe = collections.namedtuple("Recipe", ["ingredients", "allergens"])


if __name__ == "__main__":
    recipes = []
    for line in sys.stdin.readlines():
        l = line.split(" (")
        ingredients = l[0].split(" ")
        allergens = []
        if len(l) > 1:
            allergens = (
                l[1]
                .strip()
                .replace(")", "")
                .replace(",", "")
                .replace("contains ", "")
                .split(" ")
            )
        recipes.append(Recipe(ingredients, allergens))

    all_ingredients = sum([r.ingredients for r in recipes], start=[])
    all_allergens = sum([r.allergens for r in recipes], start=[])

    allergens_for_ingredient = {}

    for ingredient in all_ingredients:
        not_allergs = set(
            sum(
                [r.allergens for r in recipes if ingredient not in r.ingredients],
                start=[],
            )
        )
        possible_allergs = set(all_allergens) - not_allergs
        if possible_allergs:
            allergens_for_ingredient[ingredient] = possible_allergs

    # Part 1 answer is the total count of non-allergen ingredients
    ok_ingredients = collections.defaultdict(lambda: 0)
    for ingredient in all_ingredients:
        if ingredient not in potential_allergens_for_ingredient:
            ok_ingredients[ingredient] += 1
    print("Part 1:", sum(ok_ingredients.values()))

    allergen_map = {}
    while len(allergen_map) != len(set(all_allergens)):
        for ingredient in (
            i for i in allergens_for_ingredient if i not in allergen_map
        ):
            potential_allergens = list(
                a
                for a in potential_allergens_for_ingredient[ingredient]
                if a not in allergen_map.values()
            )
            if len(potential_allergens) == 1:
                allergen_map[ingredient] = potential_allergens.pop()

    ordered_ingredients = sorted(
        (k for k in allergen_map.keys()), key=lambda i: allergen_map[i]
    )
    print("Part 2:", ",".join(ordered_ingredients))
