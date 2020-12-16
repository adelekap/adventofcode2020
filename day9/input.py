from typing import List

from utils.input_utils import read_input


def read_xmas_input() -> List[int]:
    raw_input = read_input(day=9)
    return [int(i) for i in raw_input]
