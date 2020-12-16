from typing import List

from day8.instruction import Instruction


class Code:
    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions
        self.executed_instructions = set()
        self.last_executed_instruction = None
        self.accumulator = 0

    def _find_loop(self, line: int):
        if line >= len(self.instructions) or self.instructions[line] in self.executed_instructions:
            return

        instruction = self.instructions[line]
        self.accumulator, next_line = instruction.execute(self.accumulator)
        self.executed_instructions.add(instruction)
        self.last_executed_instruction = instruction

        return self._find_loop(next_line)

    def run_code(self):
        self._find_loop(0)

    def terminated(self) -> bool:
        return self.last_executed_instruction == self.instructions[-1]

    def reset_code(self):
        self.accumulator = 0
        self.last_executed_instruction = None
        self.executed_instructions = set()
