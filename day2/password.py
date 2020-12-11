from dataclasses import dataclass

from day2.rule import PasswordOccurrenceRule


@dataclass
class Password:
    input_string: str

    @property
    def password(self) -> str:
        return self.input_string.split(':')[-1]

    @property
    def rule(self) -> PasswordOccurrenceRule:
        return PasswordOccurrenceRule(self.input_string.split(':')[0])

    def is_valid_password(self) -> bool:
        return self.rule.validate(self.password)
