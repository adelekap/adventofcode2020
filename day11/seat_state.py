from copy import deepcopy
from dataclasses import dataclass
from typing import Type, List, Optional

from day11.seat import Seat


@dataclass
class SeatState:
    t: int
    previous_state: Optional[Type["SeatState"]]
    seat_grid: List[List[Seat]]

    @property
    def occupied_seats(self) -> int:
        return len([seat for row in self.seat_grid for seat in row if seat.is_occupied])

    @property
    def is_stagnant(self) -> bool:
        return self.previous_state and self.previous_state.seat_grid == self.seat_grid

    def _valid_seat(self, coordinate: tuple) -> bool:
        row_valid = coordinate[0] >= 0 and (coordinate[0] < len(self.seat_grid))
        column_valid = coordinate[1] >= 0 and (coordinate[1] < len(self.seat_grid[0]))
        return row_valid and column_valid

    def _adjacent_seats(self, coordinate: tuple) -> list:
        row, column = coordinate
        potential_seats = [(row, column - 1), (row - 1, column), (row, column + 1), (row + 1, column),
                           (row - 1, column - 1), (row - 1, column + 1), (row + 1, column - 1), (row + 1, column + 1)]
        return [self.seat_grid[s[0]][s[1]] for s in potential_seats if self._valid_seat(s)]

    def _apply_seat_rules(self) -> List[list]:
        new_seats = deepcopy(self.seat_grid)

        for row in range(len(new_seats)):
            for column in range(len(new_seats[0])):
                seat = new_seats[row][column]

                adjacent_seats = self._adjacent_seats((row, column))
                num_occupied_adjacent = len([s for s in adjacent_seats if s.is_occupied])

                if seat.is_empty and num_occupied_adjacent == 0:
                    seat.occupy_seat()
                elif seat.is_occupied and num_occupied_adjacent >= 4:
                    seat.empty_seat()
        return new_seats

    def generate_next_state(self) -> Type["SeatState"]:
        return SeatState(self.t + 1, self, self._apply_seat_rules())
