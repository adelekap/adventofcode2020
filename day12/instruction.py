from dataclasses import dataclass

import day12.boat_mechanics as mechanics

from day12.ferry_state import FerryState


@dataclass
class Instruction:
    input_str: str

    @property
    def direction(self) -> str:
        return self.input_str[0]

    @property
    def value(self) -> int:
        return int(self.input_str[1:])

    def carry_out_instruction(self, state: FerryState):
        if self.direction == 'F':
            return FerryState(state.t + 1, state.heading,
                              mechanics.new_position(state.heading, state.position, self.value))
        if self.direction in mechanics.HEADINGS:
            return FerryState(state.t + 1, state.heading,
                              mechanics.new_position(self.direction, state.position, self.value))

        new_heading = mechanics.change_heading(state.heading, self.direction, self.value)
        return FerryState(state.t + 1, new_heading, state.position)
