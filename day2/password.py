from collections import Counter
from dataclasses import dataclass

from day2.rule import PasswordRule


@dataclass
class Password:
    input_string: str

    @property
    def password(self) -> str:
        return self.input_string.split(':')[-1]

    @property
    def rule(self) -> PasswordRule:
        return PasswordRule(self.input_string.split(':')[0])

    @property
    def occurrences(self) -> Counter:
        return Counter(self.password)

    def is_valid_password(self) -> bool:
        actual_appearances = self.occurrences.get(self.rule.restricted_letter, 0)
        return self.rule.lowest_appearances <= actual_appearances <= self.rule.highest_appearances
