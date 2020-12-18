from dataclasses import dataclass

EMPTY_SEAT = "L"
OCCUPIED_SEAT = "#"
FLOOR = "."


@dataclass
class Seat:
    value: str

    @property
    def is_occupied(self) -> bool:
        return self.value == OCCUPIED_SEAT

    @property
    def is_empty(self) -> bool:
        return self.value == EMPTY_SEAT

    def occupy_seat(self):
        self.value = OCCUPIED_SEAT

    def empty_seat(self):
        self.value = EMPTY_SEAT

    def __eq__(self, other):
        return other.value == self.value

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.value
