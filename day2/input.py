from typing import List

from day2.password import Password
from utils.input_utils import read_input


def read_password_input() -> List[Password]:
    puzzle_input = read_input(2)
    return [Password(i) for i in puzzle_input]
