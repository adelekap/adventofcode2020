from dataclasses import dataclass
from math import cos, sin, radians


@dataclass
class Waypoint:
    t: int
    position: tuple
    distance_from_ship: tuple

    def rotate(self, action: str, angle: int):
        ferry_point = ((self.position[0] - self.distance_from_ship[0]),
                       self.position[1] - self.distance_from_ship[1])

        x, y = self.distance_from_ship
        angle = radians(angle)

        if action == 'R':
            distance_from_ship = (int(round(x * cos(angle) + y * sin(angle), 0)),
                                  int(round(y * cos(angle) - x * sin(angle), 0)))

            position = ((ferry_point[0] + self.distance_from_ship[0]),
                        ferry_point[1] + self.distance_from_ship[1])

        else:
            distance_from_ship = (int(round(x * cos(angle) - y * sin(angle), 0)),
                                  int(round(x * sin(angle) + y * cos(angle), 0)))

            position = ((ferry_point[0] + self.distance_from_ship[0]),
                        ferry_point[1] + self.distance_from_ship[1])

        return Waypoint(self.t + 1, position, distance_from_ship)
