from day11.input import read_seat_input
from day11.seat_state import SeatState


def state_when_seats_dont_change() -> SeatState:
    state = read_seat_input()

    while not state.is_stagnant:
        state = state.generate_next_state()

    return state


if __name__ == '__main__':
    stagnant_state = state_when_seats_dont_change()
    print(stagnant_state.occupied_seats)