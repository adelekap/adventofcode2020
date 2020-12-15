from typing import List

from day4.input import read_passport_input
from day4.passport import Passport


def validate_passports() -> List[Passport]:
    puzzle_input = read_passport_input()
    passports = [Passport(i) for i in puzzle_input]
    valid_passports = [p for p in passports if p.valid()]

    return valid_passports


if __name__ == '__main__':
    print(f"{len(validate_passports())} valid passports")
