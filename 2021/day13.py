import utils
from collections import namedtuple

Paper = namedtuple('Paper', ['dots', 'instructions'])

def to_paper(data):
    dots = frozenset([
        (int(x), int(y)) for line in data
        for x,y in line.split(',')
        if ',' in line
    ])

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

    return new_dots

def fold_along_y(y_val, dots):
    new_dots = set()
    for d in dots:
        if d[1] > y_val:
            diff = d[1] - y_val
            new_dots |= {(d[0], y_val - diff)}

    return new_dots

def fold(dots, instruction):
    x, y = instruction
    if x != 0:
        return fold_along_x(x, dots)
    else:
        return fold_along_y(y, dots)

def process_one_instruction(paper):
    return fold(paper.dots, paper.instructions[0])

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

print(len(process_one_instruction((to_paper(test_data)))))
