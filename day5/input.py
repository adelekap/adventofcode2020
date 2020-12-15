from typing import List

from day5.boarding_pass import BoardingPass
from utils.input_utils import read_input


def read_boarding_pass_input() -> List[BoardingPass]:
    raw_input = read_input(day=5)

    return [BoardingPass(i) for i in raw_input]
