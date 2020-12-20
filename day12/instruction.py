from dataclasses import dataclass

import day12.boat_mechanics as mechanics

from day12.ferry_state import FerryState
from day12.waypoint import Waypoint


@dataclass
class Instruction:
    input_str: str

    @property
    def action(self) -> str:
        return self.input_str[0]

    @property
    def value(self) -> int:
        return int(self.input_str[1:])

    def carry_out_instruction(self, state: FerryState):
        if self.action == 'F':
            return FerryState(state.t + 1, state.heading,
                              mechanics.new_position(state.heading, state.position, self.value))
        if self.action in mechanics.HEADINGS:
            return FerryState(state.t + 1, state.heading,
                              mechanics.new_position(self.action, state.position, self.value))

        new_heading = mechanics.change_heading(state.heading, self.action, self.value)
        return FerryState(state.t + 1, new_heading, state.position)

    def carry_out_instructions_with_waypoint(self, state: FerryState, waypoint: Waypoint) -> tuple:
        if self.action == 'F':
            new_ferry_state = FerryState(state.t + 1, state.heading, (state.position[0] +
                                                                      self.value * waypoint.distance_from_ship[0],
                                                                      state.position[1] +
                                                                      self.value * waypoint.distance_from_ship[1]))
            new_waypoint_state = Waypoint(waypoint.t + 1,
                                          (new_ferry_state.position[0] + waypoint.distance_from_ship[0],
                                           new_ferry_state.position[1] + waypoint.distance_from_ship[1]),
                                          waypoint.distance_from_ship)

        elif self.action in mechanics.HEADINGS:
            new_ferry_state = FerryState(state.t + 1, state.heading, state.position)
            new_waypoint_state = Waypoint(waypoint.t + 1, mechanics.new_position(self.action,
                                                                                 waypoint.position,
                                                                                 self.value),
                                          mechanics.new_position(self.action, waypoint.distance_from_ship, self.value))

        else:
            new_ferry_state = FerryState(state.t + 1, state.heading, state.position)
            new_waypoint_state = waypoint.rotate(self.action, self.value)

        return new_ferry_state, new_waypoint_state
