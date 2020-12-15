from typing import List, Dict

from day7.bag import Bag


class BaggageRules:
    def __init__(self, rules_input: List[str]):
        self.rules_input = rules_input

        self._bags = {}

    @property
    def bags(self) -> Dict[str, Bag]:
        if not self._bags:
            for rule in self.rules_input:
                self._define_outer_bag_rule(rule)

        return self._bags

    def _define_outer_bag_rule(self, rule_string: str):
        outer_bag, fragment = rule_string.split(' bags contain ')
        bag = self._bags.get(outer_bag)

        if not bag:
            bag = Bag(outer_bag)
            self._bags[outer_bag] = bag

        bag.contents = self._parse_contents(fragment)
        self._bags[outer_bag] = bag

    def _parse_contents(self, rule_string: str) -> List[Bag]:
        contents = []

        if rule_string != 'no other bags.':
            bags = rule_string.split(', ')

            for bag_info in bags:
                contents += self._define_inner_bags_rules(bag_info)

        return contents

    def _define_inner_bags_rules(self, bag_info: str) -> List[Bag]:
        components = bag_info.split(' ')
        num = int(components[0])
        color = ' '.join(components[1:-1])

        inner_bag = self._bags.get(color)

        if not inner_bag:
            inner_bag = Bag(color)
            self._bags[color] = inner_bag

        return [inner_bag] * num
