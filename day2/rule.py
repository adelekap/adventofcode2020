from dataclasses import dataclass


@dataclass
class PasswordRule:
    rule_string: str

    @property
    def restricted_letter(self) -> str:
        return self.rule_string[-1]

    @property
    def lowest_appearances(self) -> int:
        return int(self.rule_string.split('-')[0])

    @property
    def highest_appearances(self) -> int:
        return int(self.rule_string.split(' ')[0].split('-')[-1])
