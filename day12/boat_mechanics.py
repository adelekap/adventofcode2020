HEADINGS = ['N', 'E', 'S', 'W']
TURN_MAPPING = {'L': -1, 'R': 1}
POSITION_MAPPING = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}


def change_heading(current_heading: str, turn_direction: str, deg: int) -> str:
    current_index = HEADINGS.index(current_heading)
    index = current_index + TURN_MAPPING[turn_direction] * int(deg / 90)
    index = index if index < len(HEADINGS) else len(HEADINGS) - index
    return HEADINGS[index]


def new_position(direction: str, current_position: tuple, value: int) -> tuple:
    movement = POSITION_MAPPING[direction]

    return current_position[0] + movement[0] * value, current_position[1] + movement[1] * value
