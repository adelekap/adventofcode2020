from day11.seat import Seat
from day11.seat_state import SeatState
from utils.input_utils import read_input


def read_seat_input() -> SeatState:
    raw_input = read_input(day=11)
    grid = [[Seat(s) for s in row] for row in raw_input]

    return SeatState(0, None, grid)
