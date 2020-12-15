from typing import List

from day5.boarding_pass import ROWS, COLUMNS
from day5.input import read_boarding_pass_input
from utils.exceptions import InfeasibleSolutionException


def all_seat_ids() -> List[int]:
    boarding_passes = read_boarding_pass_input()
    return [p.seat_id for p in boarding_passes]


def highest_seat() -> int:
    return max(all_seat_ids())


def determine_your_seat() -> int:
    seat_ids = set(all_seat_ids())
    missing_seat_ids = set(range(0, (ROWS - 1) * 8 + (COLUMNS - 1))) - seat_ids

    for seat_id in missing_seat_ids:
        if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
            return seat_id

    raise InfeasibleSolutionException


if __name__ == '__main__':
    print(highest_seat())

    print(determine_your_seat())
