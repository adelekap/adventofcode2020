from typing import List

from collections import defaultdict


class Bag:
    def __init__(self, color: str, contents: list = None):
        self.color = color
        self.contents = contents or []

        self.__contents_count = None

    @property
    def contents_count(self) -> dict:
        if self.__contents_count is None:
            self.__contents_count = defaultdict(int)

            for bag in self.contents:
                self.__contents_count[bag.color] += 1

                for color, count in bag.contents_count.items():
                    self.__contents_count[color] += count

        return self.__contents_count

    def number_of_bags_inside(self, color: str) -> int:
        return self.contents_count[color]

    def __hash__(self):
        return self.color

    def __eq__(self, other):
        return self.color == other.color

    def __repr__(self):
        return f'{self.color}: {len(self.contents)} bags inside'
