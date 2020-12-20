from day13.input import read_bus_input


def find_earliest_bus() -> tuple:
    earliest_departure, buses = read_bus_input()
    in_service_buses = [b for b in buses if not b.out_of_service]

    time = earliest_departure

    while time:
        for bus in in_service_buses:
            if bus.arrives(time):
                return bus, time - earliest_departure
        time += 1


if __name__ == '__main__':
    earliest_bus, waiting_minutes = find_earliest_bus()

    print(earliest_bus.frequency * waiting_minutes)
