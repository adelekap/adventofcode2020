from copy import deepcopy
from dataclasses import dataclass
from typing import Type, List, Optional, Callable

from day11.seat import Seat


@dataclass
class SeatState:
    t: int
    previous_state: Optional[Type["SeatState"]]
    seat_grid: List[List[Seat]]
    adjacent_rule: bool = True

    @property
    def directions(self) -> list:
        return [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    @property
    def occupied_seats(self) -> int:
        return len([seat for row in self.seat_grid for seat in row if seat.is_occupied])

    @property
    def is_stagnant(self) -> bool:
        return self.previous_state and self.previous_state.seat_grid == self.seat_grid

    @property
    def tolerance(self) -> int:
        return 4 if self.adjacent_rule else 5

    def _valid_seat(self, coordinate: tuple) -> bool:
        row_valid = coordinate[0] >= 0 and (coordinate[0] < len(self.seat_grid))
        column_valid = coordinate[1] >= 0 and (coordinate[1] < len(self.seat_grid[0]))
        return row_valid and column_valid

    def _find_seat_in_view(self, coordinate: tuple, direction: tuple, view=1) -> list:
        row, column = coordinate
        seats = []

        for n in range(1, view + 1):
            next_coordinate = (row + (direction[0] * n), column + (direction[1] * n))

            if self._valid_seat(next_coordinate):
                seat = self.seat_grid[next_coordinate[0]][next_coordinate[1]]
                seats.append(seat)

                if seat.is_occupied or seat.is_empty:
                    return seats

            else:
                return seats

        return seats

    def _seats_in_view(self, coordinate: tuple, view: int = 1) -> list:
        potential_seats = []
        for direction in self.directions:
            potential_seats += self._find_seat_in_view(coordinate, direction, view)
        return potential_seats

    def _apply_seat_rules(self, view: int) -> List[list]:
        new_seats = deepcopy(self.seat_grid)

        for row in range(len(new_seats)):
            for column in range(len(new_seats[0])):
                seat = new_seats[row][column]

                adjacent_seats = self._seats_in_view((row, column), view)
                num_occupied_adjacent = len([s for s in adjacent_seats if s.is_occupied])

                if seat.is_empty and num_occupied_adjacent == 0:
                    seat.occupy_seat()
                elif seat.is_occupied and num_occupied_adjacent >= self.tolerance:
                    seat.empty_seat()
        return new_seats

    def generate_next_state(self) -> Type["SeatState"]:
        view = 1 if self.adjacent_rule else max([len(self.seat_grid), len(self.seat_grid[0])])
        return SeatState(self.t + 1, self, self._apply_seat_rules(view), self.adjacent_rule)
