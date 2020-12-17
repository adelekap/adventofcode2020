from typing import List

from utils.input_utils import read_input


def read_sorted_joltage_input() -> List[int]:
    raw_input = read_input(day=10)
    return sorted([int(i) for i in raw_input])
