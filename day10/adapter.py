from dataclasses import dataclass


@dataclass
class Adapter:
    joltage: int
    possible_connections: list
