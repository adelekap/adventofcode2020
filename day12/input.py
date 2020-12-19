from typing import List

from day12.instruction import Instruction
from utils.input_utils import read_input


def read_navigation_instructions() -> List[Instruction]:
    input = read_input(day=12)

    return [Instruction(i) for i in input]
