from day6.input import read_customs_answer_input


def sum_of_anyone_positive_answer_counts() -> int:
    group_answers = read_customs_answer_input()
    positive_answer_counts = [a.number_of_any_positive_answers() for a in group_answers]

    return sum(positive_answer_counts)


def sum_of_all_positive_answer_counts() -> int:
    group_answers = read_customs_answer_input()
    positive_answer_counts = [a.number_of_all_positive_answers() for a in group_answers]

    return sum(positive_answer_counts)


if __name__ == '__main__':
    print(sum_of_anyone_positive_answer_counts())
    print(sum_of_all_positive_answer_counts())
