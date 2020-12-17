from collections import Counter
from typing import List

from day10.input import read_sorted_joltage_input

OUTLET_JOLTAGE = 0


class JoltageChain:
    def __init__(self, adapters: List[int]):
        self.adapters = [OUTLET_JOLTAGE] + adapters

        self.__differences = None
        self.__difference_counts = None

    @property
    def difference_counts(self) -> Counter:
        if self.__differences is None:
            self._chain_together()

        if self.__difference_counts is None:
            self.__difference_counts = Counter(self.__differences)

        return self.__difference_counts

    def _chain_together(self):
        self.__differences = []

        for n in range(1, len(self.adapters)):
            adapter = self.adapters[n]
            diff = adapter - self.adapters[n - 1]

            if diff > 3:
                break

            self.__differences.append(diff)

        self.__differences.append(3)

    def jolt_difference_multiplied(self) -> int:
        return self.difference_counts.get(1, 0) * self.difference_counts.get(3, 0)


if __name__ == '__main__':
    puzzle_input = read_sorted_joltage_input()
    chain = JoltageChain(puzzle_input)

    print(chain.difference_counts)
    print(chain.jolt_difference_multiplied())
