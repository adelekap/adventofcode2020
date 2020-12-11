from collections import Counter

from dataclasses import dataclass


@dataclass
class PasswordOccurrenceRule:
    rule_string: str

    @property
    def restricted_letter(self) -> str:
        return self.rule_string[-1]

    @property
    def lowest_occurrences(self) -> int:
        return int(self.rule_string.split('-')[0])

    @property
    def highest_occurrences(self) -> int:
        return int(self.rule_string.split(' ')[0].split('-')[-1])

    def validate(self, password: str) -> bool:
        occurrences = Counter(password)
        actual_appearances = occurrences.get(self.restricted_letter, 0)

        return self.lowest_occurrences <= actual_appearances <= self.highest_occurrences
