import os


def clean_input(raw_input: list) -> list:
    return [int(i.replace('/n', '')) for i in raw_input]


def read_input() -> list:
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(f'{dir_path}/input.txt', 'r') as f_input:
        puzzle_input = f_input.readlines()

    return clean_input(puzzle_input)
