from day9.input import read_xmas_input
from utils.exceptions import InfeasibleSolutionException

PREAMBLE_SIZE = 25


def find_contiguous_sum_n(target_sum: int) -> list:
    options = read_xmas_input()

    for n in range(len(options)):
        working_sum = options[n]
        i = n + 1

        while working_sum < target_sum and i < len(options):
            working_sum += options[i]
            i += 1

        if working_sum == target_sum:
            return options[n:i]

    raise InfeasibleSolutionException


def find_sum_in_window(target_sum: int, options: list) -> tuple:
    if len(options) >= 2:
        sum = options[0] + options[-1]

        if sum == target_sum:
            return options[0], options[-1]

        if sum > target_sum:
            return find_sum_in_window(target_sum, options[:-1])

        return find_sum_in_window(target_sum, options[1:])


def sum_possible(sum: int, options: list) -> bool:
    result = find_sum_in_window(sum, sorted([o for o in options if o <= sum]))

    return result is not None


def find_xmas_flaw() -> int:
    port_output = read_xmas_input()

    for n in range(PREAMBLE_SIZE, len(port_output)):
        number = port_output[n]
        window = port_output[n - PREAMBLE_SIZE:n]

        if not sum_possible(number, window):
            return number

    raise InfeasibleSolutionException


def find_encryption_weakness() -> int:
    xmas_flaw = find_xmas_flaw()
    contiguous_sum_n = find_contiguous_sum_n(xmas_flaw)
    sorted_n = sorted(contiguous_sum_n)

    return sorted_n[0] + sorted_n[-1]


if __name__ == '__main__':
    print(find_xmas_flaw())

    print(find_encryption_weakness())
