from day9.input import read_xmas_input
from utils.exceptions import InfeasibleSolutionException

PREAMBLE_SIZE = 25


def find_sum(target_sum, options: list) -> tuple:
    if len(options) >= 2:
        sum = options[0] + options[-1]

        if sum == target_sum:
            return options[0], options[-1]

        if sum > target_sum:
            return find_sum(target_sum, options[:-1])

        return find_sum(target_sum, options[1:])


def sum_possible(sum: int, options: list) -> bool:
    result = find_sum(sum, sorted([o for o in options if o <= sum]))

    return result is not None


def find_xmas_flaw() -> int:
    port_output = read_xmas_input()

    for n in range(PREAMBLE_SIZE, len(port_output)):
        number = port_output[n]
        window = port_output[n - PREAMBLE_SIZE:n]

        if not sum_possible(number, window):
            return number

    raise InfeasibleSolutionException


if __name__ == '__main__':
    print(find_xmas_flaw())
