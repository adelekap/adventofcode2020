from typing import List

from day3.input import read_terrain_input
from day3.terrain import Terrain
from day3.toboggan import Toboggan
from utils.math_utils import multiply_list

TREE = '#'


def count_trees_seen(starting_position: tuple, movement_rule: List[List[int]]) -> int:
    terrain = Terrain(read_terrain_input())
    toboggan = Toboggan(starting_position, movement_rule, terrain)
    landmarks = toboggan.traverse()

    return landmarks.count(TREE)


if __name__ == '__main__':
    START = (0, 0)
    RULES = [[[0, 1], [1, 0]], [[0, 3], [1, 0]], [[0, 5], [1, 0]], [[0, 7], [1, 0]], [[0, 1], [2, 0]]]

    trees_seen = [count_trees_seen(START, rule) for rule in RULES]

    print(trees_seen)
    print()
    print(multiply_list(trees_seen))
