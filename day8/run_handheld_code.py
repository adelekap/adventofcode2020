from day8.game_console_code import Code
from day8.input import read_code_input
from utils.exceptions import InfeasibleSolutionException

INPUT = read_code_input()


def find_loop() -> int:
    code = Code(INPUT)
    code.run_code()

    if not code.terminated():
        return code.accumulator

    raise InfeasibleSolutionException


def remove_loop():
    code = Code(INPUT)

    for line in range(len(INPUT)):
        instruction = code.instructions[line]
        if instruction.can_be_changed:
            code.reset_code()
            instruction.change_command()
            code.run_code()

            if code.terminated():
                return code.accumulator

            else:
                instruction.change_command()

    raise InfeasibleSolutionException


if __name__ == '__main__':
    print(find_loop())

    print(remove_loop())
