from collections import Counter
from typing import List

from day10.input import read_sorted_joltage_input
from day10.adapter import Adapter

OUTLET_JOLTAGE = 0


class JoltageChain:
    def __init__(self, adapters: List[int]):
        self.adapters = [Adapter(a) for a in [OUTLET_JOLTAGE] + adapters]
        self.outlet = None

        self.__differences = None
        self.__difference_counts = None
        self.__valid_connections = None

        self._get_valid_connections()

    @property
    def differences(self) -> list:
        if self.__differences is None:
            self.__differences = []

            for n in range(1, len(self.adapters)):
                adapter = self.adapters[n]
                diff = adapter.joltage - self.adapters[n - 1].joltage

                if diff > 3:
                    break

                self.__differences.append(diff)

            self.__differences.append(3)
        return self.__differences

    @property
    def difference_counts(self) -> Counter:
        if self.__difference_counts is None:
            self.__difference_counts = Counter(self.differences)
        return self.__difference_counts

    @property
    def num_chain_permutations(self) -> int:
        return self.all_valid_chains(self.adapters[0], 0)

    @property
    def valid_connection(self) -> dict:
        return self.__valid_connections

    def _get_valid_connections(self):
        self.__valid_connections = {a: self._find_valid_connections(a) for a in self.adapters}

        for node, connections in self.__valid_connections.items():
            node.downstream_connections = self.__valid_connections[node]
            for connection in connections:
                connection.downstream_connections = self.__valid_connections[connection]
                connection.upstream_connections.append(node)

    def _find_valid_connections(self, adapter: Adapter) -> List[Adapter]:
        return [a for a in self.adapters if adapter.joltage < a.joltage <= adapter.joltage + 3]

    def jolt_difference_multiplied(self) -> int:
        return self.difference_counts.get(1, 0) * self.difference_counts.get(3, 0)

    def all_valid_chains(self, adapter: Adapter, count: int, ) -> int:
        if not adapter.downstream_connections:
            return count + 1

        for connection in adapter.downstream_connections:
            count = self.all_valid_chains(connection, count)

        return count


if __name__ == '__main__':
    puzzle_input = read_sorted_joltage_input()
    chain = JoltageChain(puzzle_input)

    print(chain.difference_counts)
    print(chain.jolt_difference_multiplied())

    print(chain.num_chain_permutations)
