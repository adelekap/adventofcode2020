from utils.input_utils import read_input


def read_expense_input() -> list:
    return sorted([int(i) for i in read_input(1)])
