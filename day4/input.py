from typing import List

from utils.input_utils import read_input


def read_passport_input() -> List[str]:
    input = read_input(4)

    passport_inputs = []
    passport_info = ""

    for i in input:
        if i:
            space = " " if passport_info else ""
            passport_info += f"{space}{i}"
        else:
            passport_inputs.append(passport_info)
            passport_info = ""

    passport_inputs.append(passport_info)

    return passport_inputs
