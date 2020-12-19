from dataclasses import dataclass


@dataclass
class FerryState:
    t: int
    heading: str
    position: tuple
