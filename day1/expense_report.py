from day1.expense_report_exceptions import InfeasibleSolutionException
from day1.input import read_input

TARGET_VALUE = 2020


def filter_out_high_end(expenses: list) -> list:
    return sorted(list(filter(lambda e: e < TARGET_VALUE, expenses)))


def find_target_sum_entries(expenses: list) -> list:
    if len(expenses):
        expense1 = expenses[0]
        expense2 = expenses[-1]
        expense_sum = expense1 + expense2

        if expense_sum == TARGET_VALUE:
            return [expense1, expense2]
        if expense_sum > TARGET_VALUE:
            return find_target_sum_entries(expenses[:-1])

        return find_target_sum_entries(expenses[1:])

    raise InfeasibleSolutionException


def find_solution():
    puzzle_input = read_input()
    filtered_input = filter_out_high_end(puzzle_input)
    expense1, expense2 = find_target_sum_entries(filtered_input)

    return expense1 * expense2


if __name__ == '__main__':
    solution = find_solution()

    print(solution)
