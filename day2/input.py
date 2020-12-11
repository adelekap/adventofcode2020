from typing import List, TypeVar

from day2.password import Password
from utils.input_utils import read_input


def read_password_input(rule_type: TypeVar) -> List[Password]:
    puzzle_input = read_input(2)
    return [Password(i, rule_type) for i in puzzle_input]
