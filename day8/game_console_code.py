from typing import List

from day8.instruction import Instruction


class Code:
    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions
        self.executed_instructions = set()
        self.last_executed_instruction = None
        self.accumulator = 0

    def _find_loop(self, instruction: Instruction):
        if instruction in self.executed_instructions or instruction.line >= len(self.instructions):
            self.last_executed_instruction = instruction
            return

        self.accumulator, line = instruction.execute(self.accumulator)
        self.executed_instructions.add(instruction)

        return self._find_loop(self.instructions[line])

    def run_code(self):
        self._find_loop(self.instructions[0])

    def terminated(self) -> bool:
        return self.last_executed_instruction == self.instructions[-1]
