from day13.bus import Bus
from utils.input_utils import read_input


def read_bus_input() -> tuple:
    raw_input = read_input(day=13)

    earliest_bus = int(raw_input[0])
    buses = [Bus(b) for b in raw_input[1].split(',')]

    return earliest_bus, buses
