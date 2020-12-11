from typing import List

from utils.input_utils import read_input


def read_terrain_input() -> List[List[str]]:
    input = read_input(3)
    terrain_input = []

    for row in input:
        terrain_input.append([i for i in row])

    return terrain_input
