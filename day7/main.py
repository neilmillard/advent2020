import re

from lib import get_lines_from_file


def get_bag_rule(bag):
    result = {'number': 1,
              'color': ""
              }
    words = bag.split()
    # the last word is always 'bags'
    if words[0] == 'no':
        return {}
    if words[0].isdigit() and len(words) == 4:
        result['number'] = words[0]
        result['color'] = words[1] + ' ' + words[2]
    else:
        result['color'] = words[0] + ' ' + words[1]
    return result


def get_rules(lines):
    """
    Rules are in a structure of:
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    <color> bags contain <int> <color> bags, <int> <color> bags.
    Feels like a dict of dict?
    { "<color":[
        "<color>": "<int>",
        "<color>": "<int>"
        ]
    }
    """
    rules = {}
    for line in lines:
        if line.strip():
            outer, contain = line.strip().split(' contain')
            big_bag = get_bag_rule(outer)['color']
            bags = contain.split(', ')
            coded_bags = {}
            for bag in bags:
                i = get_bag_rule(bag)
                if len(i)>0:
                    coded_bags[i['color']] = int(i['number'])
            rules[big_bag] = coded_bags

    return rules


def get_bag_data(lines):
    bags = {}
    outer_bag_pattern = r"(^\w+ \w+ \w+)"
    inner_bag_pattern = r"(\d \w+ \w+ \w+)"
    for line in lines:
        if line.strip():
            inner_bags = {}
            for inner_bag in re.findall(inner_bag_pattern, line):
                bag_count = int(inner_bag[0])
                bag_name = inner_bag[2:] if bag_count == 1 else inner_bag[2:-1]
                inner_bags[bag_name] = bag_count
            outer_bag_str = re.match(outer_bag_pattern, line).group(1)
            if outer_bag_str[-1] == "s":
                outer_bag = outer_bag_str[:-1]
            else:
                outer_bag = outer_bag_str
            bags[outer_bag] = inner_bags
    return bags


def part_a(bags, color='shiny gold'):
    holds_shiny_gold = {}

    def bag_search(bag_type):
        current_bag = bags[bag_type]
        if color in current_bag:
            holds_shiny_gold[bag_type] = True
            return True

        current_bag_search = []
        for bag in current_bag:
            if holds_shiny_gold.get(bag):
                current_bag_search.append(holds_shiny_gold.get(bag))
            else:
                current_bag_search.append(bag_search(bag))
        holds_gold = any(current_bag_search)
        holds_shiny_gold[bag_type] = holds_gold
        return holds_gold

    for bag in bags:
        bag_search(bag)

    return sum(holds_shiny_gold.values())


def part_b(bags, color='shiny gold'):
    bag_count = {}

    def count_bags(bag_to_count):
        current_bag = bags[bag_to_count]
        inner_bag_count: list[int] = []
        for bag in current_bag:
            inner_bag_count.append(current_bag[bag] * 1)
            if bag_count.get(bag):
                inner_bag_count.append(bag_count[bag] * current_bag[bag])
            else:
                inner_bag_count.append(count_bags(bag) * current_bag[bag])
        total_bags = sum(inner_bag_count)
        bag_count[bag_to_count] = total_bags
        return total_bags

    shiny_gold_bag_count = count_bags(color)
    return shiny_gold_bag_count


def day_seven():
    lines = get_lines_from_file('day7/day7.txt', True)
    rules = get_rules(lines)

    # Step 1
    # How many bag colors can eventually contain at least one shiny gold bag?
    # Test Data = 4

    print(part_a(rules))
    print(part_b(rules))

