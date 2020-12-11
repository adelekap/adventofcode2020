from dataclasses import dataclass
from typing import List


@dataclass
class Terrain:
    forest_rows: List[List[str]]

    @property
    def edge_of_forest_code(self) -> int:
        return len(self.forest_rows[0])

    def landmark_at_position(self, position: tuple) -> str:
        return self.forest_rows[position[0]][position[1]]

    def at_bottom_of_slope(self, position: tuple) -> bool:
        return position[0] >= len(self.forest_rows) - 1
