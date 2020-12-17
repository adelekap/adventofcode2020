from collections import Counter
from typing import List

from day10.input import read_sorted_joltage_input
from day10.adapter import Adapter

OUTLET_JOLTAGE = 0


class JoltageChain:
    def __init__(self, adapters: List[int]):
        self.adapters = [OUTLET_JOLTAGE] + adapters

        self.__chain_permutations = 0
        self.__differences = None
        self.__difference_counts = None
        self.__outlet = None

    @property
    def chain_permuations(self) -> int:
        if self.outlet:
            return self.__chain_permutations

        return 0

    @property
    def differences(self) -> list:
        if self.__differences is None:
            self.__differences = []

            for n in range(1, len(self.adapters)):
                adapter = self.adapters[n]
                diff = adapter - self.adapters[n - 1]

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
    def outlet(self) -> Adapter:
        if self.__outlet is None:
            self.__outlet = Adapter(0, self._find_valid_connections(0))
        return self.__outlet

    def _find_valid_connections(self, joltage: int) -> List[Adapter]:
        connections = []

        for a in self.adapters:
            if joltage < a <= joltage + 3:
                adapter = Adapter(a, self._find_valid_connections(a))
                if not adapter.possible_connections:
                    self.__chain_permutations += 1
                connections.append(adapter)
        return connections

    def jolt_difference_multiplied(self) -> int:
        return self.difference_counts.get(1, 0) * self.difference_counts.get(3, 0)


if __name__ == '__main__':
    puzzle_input = read_sorted_joltage_input()
    chain = JoltageChain(puzzle_input)

    print(chain.difference_counts)
    print(chain.jolt_difference_multiplied())

    print(chain.chain_permuations)
