from dataclasses import dataclass
from typing import TypeVar

from day2.rules import PasswordOccurrenceRule


@dataclass
class Password:
    input_string: str
    RuleType: TypeVar

    @property
    def password(self) -> str:
        return self.input_string.split(':')[-1].replace(' ', '')

    @property
    def rule(self) -> PasswordOccurrenceRule:
        return self.RuleType(self.input_string.split(':')[0])

    def is_valid_password(self) -> bool:
        return self.rule.validate(self.password)
