from dataclasses import dataclass
from typing import List

from day3.terrain import Terrain


@dataclass
class Toboggan:
    toboggan_position: tuple
    movement_rule: List[List[int]]
    terrain: Terrain

    def move_toboggan(self):
        row = sum([self.toboggan_position[0]] + [m[0] for m in self.movement_rule])
        column = sum([self.toboggan_position[1]] + [m[1] for m in self.movement_rule])

        if column >= self.terrain.edge_of_forest_code:
            column -= self.terrain.edge_of_forest_code

        self.toboggan_position = (row, column)

    def traverse(self) -> List[str]:
        landmarks = []

        while not self.terrain.at_bottom_of_slope(self.toboggan_position):
            self.move_toboggan()
            landmarks.append(self.terrain.landmark_at_position(self.toboggan_position))

        return landmarks
