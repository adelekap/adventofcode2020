from typing import TypeVar

from day2.input import read_password_input
import day2.rules as rules


def validate_passwords(rule_type: TypeVar):
    passwords = read_password_input(rule_type)
    valid_passwords = [p for p in passwords if p.is_valid_password()]
    return valid_passwords


def validate_with_occurrence_rule():
    return validate_passwords(rules.PasswordOccurrenceRule)


def validate_with_position_rule():
    return validate_passwords(rules.PasswordPositionRule)


if __name__ == '__main__':
    valid_occurrences = validate_with_occurrence_rule()
    print(f'{len(valid_occurrences)} valid passwords')

    valid_positions = validate_with_position_rule()
    print(f'{len(valid_positions)} valid passwords')
