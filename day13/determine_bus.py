from math import ceil
import numpy as np

from day13.input import read_bus_input


def heuristic_start(bus_ids: list) -> int:
    return np.gcd.reduce(bus_ids)


def find_earliest_bus() -> tuple:
    earliest_departure, buses = read_bus_input()
    in_service_buses = [b for b in buses if not b.out_of_service]

    time = earliest_departure

    while time:
        for bus in in_service_buses:
            if bus.arrives(time):
                return bus, time - earliest_departure
        time += 1


def find_consecutive_bus_arrival_time() -> int:
    _, buses = read_bus_input()
    eligible_buses = [(i, b) for i, b in enumerate(buses) if not b.out_of_service]

    increment = eligible_buses[0][1].frequency
    t = ceil(max([b[1].frequency for b in eligible_buses]) / increment) * increment

    while True:
        if all([b.arrives(t + i) for i, b in eligible_buses]):
            return t
        t += increment


if __name__ == '__main__':
    # earliest_bus, waiting_minutes = find_earliest_bus()
    #
    # print(earliest_bus.frequency * waiting_minutes)

    print(f'{find_consecutive_bus_arrival_time()}')
