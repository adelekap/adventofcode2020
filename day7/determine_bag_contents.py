from day7.input import read_bag_input

RULES = read_bag_input()


def find_bags_with_shiny_gold() -> list:
    bags = [b for b in RULES.bags.values() if b.number_of_bags_inside('shiny gold')]

    return bags


def find_num_bags_inside_shiny_gold() -> int:
    bags = RULES.bags['shiny gold'].contents_count

    return sum(bags.values())


if __name__ == '__main__':
    print(len(find_bags_with_shiny_gold()))

    print(find_num_bags_inside_shiny_gold())
