import os


def clean_input(raw_input: list) -> list:
    return [i.replace('\n', '') for i in raw_input]


def read_input(day: int) -> list:
    dir_path = os.path.dirname(os.path.realpath(__file__)).replace('/utils', '')

    with open(f'{dir_path}/day{day}/input.txt', 'r') as f_input:
        puzzle_input = f_input.readlines()

    return clean_input(puzzle_input)
