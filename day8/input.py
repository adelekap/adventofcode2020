from day8.instruction import Instruction
from utils.input_utils import read_input


def read_code_input() -> list:
    raw_input = read_input(day=8)
    instructions = []

    for i, input in enumerate(raw_input):
        command, param_str = input.split(' ')
        instructions.append(Instruction(i, command, int(param_str)))

    return instructions
