from dataclasses import dataclass
from collections import Counter


@dataclass
class GroupAnswer:
    input_string: str

    @property
    def answer_counts(self) -> Counter:
        return Counter(self.input_string)

    @property
    def people_in_group(self) -> int:
        return self.answer_counts.get(' ', 0) + 1

    def number_of_any_positive_answers(self) -> int:
        spaces = 1 if self.people_in_group > 1 else 0

        return len(self.answer_counts) - spaces

    def number_of_all_positive_answers(self) -> int:
        all_positive_answers = [a for a, c in self.answer_counts.items() if c == self.people_in_group]

        return len(all_positive_answers)
