from utils.exceptions import InfeasibleSolutionException
from day1.input import read_expense_input
from utils.math_utils import multiply_list


def find_target_sum_entries(expenses: list) -> list:
    if len(expenses):
        entries = expenses[:(N - 1)] + [expenses[-1]]
        expenses_sum = sum(entries)

        if expenses_sum == TARGET_VALUE:
            return entries

        if expenses_sum > TARGET_VALUE:
            return find_target_sum_entries(expenses[:-1])

        return find_target_sum_entries(expenses[1:])

    raise InfeasibleSolutionException


def find_solution():
    sorted_puzzle_input = read_expense_input()
    target_expenses = find_target_sum_entries(sorted_puzzle_input)
    print(target_expenses)

    return multiply_list(target_expenses)


if __name__ == '__main__':
    TARGET_VALUE = 2020
    N = 3

    solution = find_solution()

    print(solution)
