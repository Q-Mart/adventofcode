import utils
from collections import namedtuple

Paper = namedtuple('Paper', ['dots', 'instructions'])

def to_paper(data):
    dots = set()
    for line in data:
        if ',' in line:
            x,y = line.split(',')
            dots |= {(int(x), int(y))}

    dots = frozenset(dots)

    instructions = []
    for line in data:
        if 'fold' in line:
            line = line.split()
            axis, amount = line[-1].split('=')
            if axis == 'x':
                instructions.append((int(amount), 0))
            else:
                instructions.append((0, int(amount)))

    return Paper(dots, instructions)

def fold_along_x(x_val, dots):
    new_dots = set()
    for d in dots:
        if d[0] > x_val:
            diff = d[0] - x_val
            new_dots |= {(x_val - diff, d[1])}
        else:
            new_dots |= {d}

    return new_dots

def fold_along_y(y_val, dots):
    new_dots = set()
    for d in dots:
        if d[1] > y_val:
            diff = d[1] - y_val
            new_dots |= {(d[0], y_val - diff)}
        else:
            new_dots |= {d}

    return new_dots

def fold(dots, instruction):
    x, y = instruction
    if x != 0:
        return fold_along_x(x, dots)
    else:
        return fold_along_y(y, dots)

def process_one_instruction(paper):
    return fold(paper.dots, paper.instructions[0])

def process_all_instructions(paper):
    dots = paper.dots
    for ins in paper.instructions:
        dots = fold(dots, ins)

    return dots

def print_dots(dots):
    max_x = max([x for x, _ in dots]) + 1
    max_y = max([y for _, y in dots]) + 1

    print('\033[92m')
    for y in range(max_y):
        str = ''
        for x in range(max_x):
            if (x, y) in dots:
                str += '#'
            else:
                str += '.'

        print(str)
    print('\033[0m')

def process_all_instructions_and_print(paper):
    dots = process_all_instructions(paper)
    print_dots(dots)

test_data = [
    "6,10",
    "0,14",
    "9,10",
    "0,3",
    "10,4",
    "4,11",
    "6,0",
    "6,12",
    "4,1",
    "0,13",
    "10,12",
    "3,4",
    "3,0",
    "8,4",
    "1,10",
    "2,14",
    "8,10",
    "9,0",
    "",
    "fold along y=7",
    "fold along x=5"
]

data = utils.get_day(2021, 13)

test_paper = to_paper(test_data)
paper = to_paper(data)

assert len(process_one_instruction(test_paper)) == 17
utils.print_part_1(len(process_one_instruction(paper)))

# process_all_instructions_and_print(test_paper)
utils.print_part_1(len(process_one_instruction(paper)))
