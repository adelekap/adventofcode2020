from abc import ABC
from collections import Counter
from dataclasses import dataclass


@dataclass
class PasswordRule(ABC):
    rule_string: str

    @property
    def restricted_letter(self) -> str:
        return self.rule_string[-1]

    @property
    def low_restriction(self) -> int:
        return int(self.rule_string.split('-')[0])

    @property
    def high_restriction(self) -> int:
        return int(self.rule_string.split(' ')[0].split('-')[-1])

    def validate(self, password: str) -> bool:
        pass


@dataclass
class PasswordOccurrenceRule(PasswordRule):
    rule_string: str

    def validate(self, password: str) -> bool:
        occurrences = Counter(password)
        actual_appearances = occurrences.get(self.restricted_letter, 0)

        return self.low_restriction <= actual_appearances <= self.high_restriction


@dataclass
class PasswordPositionRule(PasswordRule):
    rule_string: str

    def validate(self, password: str) -> bool:
        search_space = [password[self.low_restriction - 1], password[self.high_restriction - 1]]
        occurrences = Counter(search_space)
        actual_appearances = occurrences.get(self.restricted_letter, 0)

        return actual_appearances == 1
