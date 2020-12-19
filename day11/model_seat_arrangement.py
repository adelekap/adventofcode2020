from day11.input import read_seat_input
from day11.seat_state import SeatState


def state_when_seats_dont_change(adjacent_rule: bool) -> SeatState:
    state = SeatState(0, None, read_seat_input(), adjacent_rule)

    while not state.is_stagnant:
        state = state.generate_next_state()

    return state


if __name__ == '__main__':
    stagnant_state_adjacent = state_when_seats_dont_change(adjacent_rule=True)
    print(stagnant_state_adjacent.occupied_seats)

    stagnant_state_view = state_when_seats_dont_change(adjacent_rule=False)
    print(stagnant_state_view.occupied_seats)
