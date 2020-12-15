from day7.input import read_bag_input


def define_bags_with_shiny_gold() -> list:
    rules = read_bag_input()
    bags = [b for b in rules.bags.values() if b.number_of_bags_inside('shiny gold')]

    return bags


if __name__ == '__main__':
    print(len(define_bags_with_shiny_gold()))
