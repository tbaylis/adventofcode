"""
Advent of code, day 4 - Passport Processing

https://adventofcode.com/2020/day/4
"""
import fileinput
import re

expected_keys = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]


def simple_passport_validator(p):
    return all(key in p for key in expected_keys)


def advanced_passport_validator(p):
    if not simple_passport_validator(p):
        return False

    if not (
        (len(p["byr"]) == 4) and (1920 <= int(p["byr"])) and (2002 >= int(p["byr"]))
    ):
        return False

    if not (
        (len(p["iyr"]) == 4) and (2010 <= int(p["iyr"])) and (2020 >= int(p["iyr"]))
    ):
        return False

    if not (
        (len(p["eyr"]) == 4) and (2020 <= int(p["eyr"])) and (2030 >= int(p["eyr"]))
    ):
        return False

    pattern_hgt = re.compile("^[0-9]+(cm|in)$")
    if not pattern_hgt.match(p["hgt"]):
        return False

    if "cm" in p["hgt"]:
        if not ((150 <= int(p["hgt"][:-2])) and (int(p["hgt"][:-2]) <= 193)):
            return False

    if "in" in p["hgt"]:
        if not ((59 <= int(p["hgt"][:-2])) and (int(p["hgt"][:-2]) <= 76)):
            return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    pattern = re.compile("^#[a-z0-9]{6}$")
    if not pattern.match(p["hcl"]):
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if not p["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid_pattern = re.compile("^[0-9]{9}$")
    if not pid_pattern.match(p["pid"]):
        return False

    # cid (Country ID) - ignored, missing or not.
    return True


if __name__ == "__main__":
    passports = []

    passport = {}
    for line in fileinput.input():
        if line == "\n":
            passports.append(passport)
            passport = {}
        else:
            passport.update(
                {kv.split(":")[0]: kv.split(":")[1] for kv in line.rstrip().split(" ")}
            )

    passports.append(passport)

    simple_validations = 0
    advanced_validations = 0
    for passport in passports:
        if simple_passport_validator(passport):
            simple_validations += 1
        if advanced_passport_validator(passport):
            advanced_validations += 1

    print(f"Found {simple_validations} simple valid passports in input")
    print(f"Found {advanced_validations} advanced valid passports in input")
