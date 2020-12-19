from day12.ferry_state import FerryState
from day12.input import read_navigation_instructions

STARTING_HEADING = 'E'


def navigate(state: FerryState, instructions: list) -> FerryState:
    if instructions:
        new_state = instructions[0].carry_out_instruction(state)

        return navigate(new_state, instructions[1:])

    return state


def determine_ending_position() -> tuple:
    instructions = read_navigation_instructions()
    starting_state = FerryState(0, STARTING_HEADING, (0, 0))
    ending_state = navigate(starting_state, instructions)

    return ending_state.position


def manhattan_distance(position: tuple) -> int:
    return abs(position[0]) + abs(position[1])


if __name__ == '__main__':
    ending_position = determine_ending_position()
    print(manhattan_distance(ending_position))
