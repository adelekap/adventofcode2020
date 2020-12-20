from day12.ferry_state import FerryState
from day12.input import read_navigation_instructions
from day12.waypoint import Waypoint

STARTING_HEADING = 'E'
WAYPOINT_STARTING_POINT = (10, 1)


def navigate(state: FerryState, instructions: list) -> FerryState:
    if instructions:
        new_state = instructions[0].carry_out_instruction(state)

        return navigate(new_state, instructions[1:])

    return state


def navigate_with_waypoint(state: FerryState, waypoint: Waypoint, instructions: list) -> FerryState:
    if instructions:
        new_state, new_waypoint = instructions[0].carry_out_instructions_with_waypoint(state, waypoint)

        return navigate_with_waypoint(new_state, new_waypoint, instructions[1:])

    return state


def determine_ending_position(with_waypoint: bool = False) -> tuple:
    instructions = read_navigation_instructions()
    starting_state = FerryState(0, STARTING_HEADING, (0, 0))

    if with_waypoint:
        starting_waypoint = Waypoint(0, WAYPOINT_STARTING_POINT, WAYPOINT_STARTING_POINT)
        ending_state = navigate_with_waypoint(starting_state, starting_waypoint, instructions)

    else:
        ending_state = navigate(starting_state, instructions)

    return ending_state.position


def manhattan_distance(position: tuple) -> int:
    return abs(position[0]) + abs(position[1])


if __name__ == '__main__':
    ending_position = determine_ending_position()
    print(manhattan_distance(ending_position))

    ending_position_with_waypoint = determine_ending_position(with_waypoint=True)
    print(manhattan_distance(ending_position_with_waypoint))
