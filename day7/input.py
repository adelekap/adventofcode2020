from day7.baggage_rules import BaggageRules
from utils.input_utils import read_input


def read_bag_input() -> BaggageRules:
    raw_input = read_input(day=7)

    return BaggageRules(raw_input)
