from dataclasses import dataclass


@dataclass
class Bus:
    frequency_str: str

    @property
    def frequency(self) -> int:
        if not self.out_of_service:
            return int(self.frequency_str)

    @property
    def out_of_service(self) -> bool:
        return self.frequency_str == 'x'

    def arrives(self, time: int) -> bool:
        if self.out_of_service:
            return False

        return time % self.frequency == 0
