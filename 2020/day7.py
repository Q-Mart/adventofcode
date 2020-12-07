import utils
import re
from collections import namedtuple

rules = utils.get_day(2020, 7)

example1 = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
           'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
           'bright white bags contain 1 shiny gold bag.',
           'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
           'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
           'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
           'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
           'faded blue bags contain no other bags.',
           'dotted black bags contain no other bags.']

example2 = ['shiny gold bags contain 2 dark red bags.',
            'dark red bags contain 2 dark orange bags.',
            'dark orange bags contain 2 dark yellow bags.',
            'dark yellow bags contain 2 dark green bags.',
            'dark green bags contain 2 dark blue bags.',
            'dark blue bags contain 2 dark violet bags.',
            'dark violet bags contain no other bags.']

Node = namedtuple('Node', ['colour', 'amount'])
parent_regex = re.compile('\w+ \w+(?= bag)')
child_regex = re.compile('(\d+) (\w+ \w+)(?= bag)')

def to_pair(line):
    bags, contains = line.split('contain')
    contains = contains.split(',')

    parent_match = parent_regex.match(bags)
    parent = parent_match.group(0)

    children = []
    for child in contains:
        if 'no other' in child:
            children.append(Node(colour=None, amount=1))
        else:
            child_match = child_regex.search(child)
            children.append(Node(colour=child_match.group(2),
                                 amount=int(child_match.group(1))))

    return {parent: children}

def construct_tree(rules):
    tree = {}
    for r in rules:
        tree = {**tree, **to_pair(r)}

    return tree

def is_parent(tree, parent, target):
    def get_children(bag_col):
        if bag_col == None:
            return []
        children = tree[bag_col]
        return [node.colour for node in children]

    def at_target(bag_col):
        return bag_col == target

    return utils.dfs(parent, at_target, get_children) == target

def find_no_parents(rules, target):
    no_parents = 0
    tree = construct_tree(rules)

    for r in rules:
        col = parent_regex.search(r).group()

        if col == target:
            continue
        elif is_parent(tree, col, target):
            no_parents += 1

    return no_parents

def get_total_bags_needed(rules, colour):
    tree = construct_tree(rules)

    def get_bags_for(colour, memo={}):
        if colour in memo:
            return memo[colour]
        elif colour == None:
            return 0

        total = 0
        for child in tree[colour]:
            total += child.amount * (get_bags_for(child.colour, memo=memo)+1)

        memo[colour] = total
        return total

    return get_bags_for(colour)


assert(find_no_parents(example1, 'shiny gold') == 4)

utils.print_part_1(find_no_parents(rules, 'shiny gold'))

print(get_total_bags_needed(example1, 'shiny gold'))
assert(get_total_bags_needed(example1, 'shiny gold') == 32)
print(get_total_bags_needed(example2, 'shiny gold'))
assert(get_total_bags_needed(example2, 'shiny gold') == 126)
