from dataclasses import dataclass

ROWS = 128
COLUMNS = 8
LOWER_INSTRUCTIONS = {'F', 'L'}
UPPER_INSTRUCTIONS = {'B', 'R'}


@dataclass
class BoardingPass:
    boarding_pass_input: str

    @property
    def column(self) -> int:
        return self._determine_position(self.boarding_pass_input[7:], COLUMNS)

    @property
    def row(self) -> int:
        return self._determine_position(self.boarding_pass_input[:7], ROWS)

    @property
    def seat_id(self) -> int:
        return (self.row * 8) + self.column

    def _determine_position(self, instructions: list, upper_bound: int, ) -> int:
        lower_bound = 0

        for instruction in instructions:
            lower_bound, upper_bound = self.bisect((lower_bound, upper_bound), instruction)

        return lower_bound

    @staticmethod
    def bisect(previous: tuple, instruction: str) -> tuple:
        lower, upper = previous
        midpoint = int(lower + (upper - lower) / 2)

        if instruction in LOWER_INSTRUCTIONS:
            return lower, midpoint

        return midpoint, upper
