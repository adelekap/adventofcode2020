from functools import reduce


def multiply_list(list_of_nums: list) -> int:
    return reduce(lambda a, b: a * b, list_of_nums)