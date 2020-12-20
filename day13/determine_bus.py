import numpy as np

from day13.input import read_bus_input


def lcm_frequencies(iter_buses: list) -> int:
    return np.lcm.reduce([b.frequency for b in iter_buses])


def find_earliest_bus() -> tuple:
    earliest_departure, buses = read_bus_input()
    in_service_buses = [b for b in buses if not b.out_of_service]

    time = earliest_departure

    while time:
        for bus in in_service_buses:
            if bus.arrives(time):
                return bus, time - earliest_departure
        time += 1


def _find_consecutive(index: int, t: int, increment: int, iter_buses: list) -> int:
    if index <= len(iter_buses) - 2:
        while True:
            arrivals = [bus.arrives(t + i) for i, bus in iter_buses[:index + 2]]

            if all(arrivals):
                new_increment = lcm_frequencies([b[1] for b in iter_buses[:index + 2]])
                return _find_consecutive(index + 1, t, new_increment, iter_buses)

            t += increment

    return t


def find_consecutive_bus_arrival_time() -> int:
    _, buses = read_bus_input()
    eligible_buses = [(i, b) for i, b in enumerate(buses) if not b.out_of_service]

    starting_t = eligible_buses[0][1].frequency

    time = _find_consecutive(0, starting_t, starting_t, eligible_buses)
    return time


if __name__ == '__main__':
    earliest_bus, waiting_minutes = find_earliest_bus()

    print(earliest_bus.frequency * waiting_minutes)
    print(f'{find_consecutive_bus_arrival_time()}')
