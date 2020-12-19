from day11.seat import Seat
from utils.input_utils import read_input


def read_seat_input() -> list:
    raw_input = read_input(day=11)
    grid = [[Seat(s) for s in row] for row in raw_input]

    return grid
