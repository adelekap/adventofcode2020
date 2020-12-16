from dataclasses import dataclass


@dataclass
class Instruction:
    line: int
    command: str
    param: int

    @property
    def can_be_changed(self) -> bool:
        return self.command == 'nop' or (self.command == 'jmp' and self.param < 0)

    def change_command(self):
        self.command = 'nop' if self.command == 'jmp' else 'jmp'

    def execute(self, accumulator: int) -> tuple:
        if self.command == 'acc':
            return accumulator + self.param, self.line + 1
        if self.command == 'jmp':
            return accumulator, self.line + self.param

        return accumulator, self.line + 1

    def __hash__(self):
        return self.line

    def __str__(self):
        return f'({self.line}) {self.command} {self.param}'

    def __repr__(self):
        return str(self)
