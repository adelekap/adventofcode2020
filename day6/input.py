from typing import List

from day6.group_answer import GroupAnswer
from utils.input_utils import read_input


def read_customs_answer_input() -> List[GroupAnswer]:
    raw_input = read_input(6)
    groups = []
    group = ""

    for individual in raw_input:
        space = " " if group else ""
        if individual:
            group += f"{space}{individual}"
        else:
            groups.append(group)
            group = ""
    groups.append(group)

    return [GroupAnswer(g) for g in groups]
