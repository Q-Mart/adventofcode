import utils
from collections import namedtuple

Node = namedtuple('Node', ['risk', 'h', 'x', 'y'])

def to_grid(data):
    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    grid = []
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            grid.append(
                Node(
                    int(c),
                    (max_x - x) + (max_y - y),
                    x,
                    y
                )
            )

    return grid

def h_func(node):
    return node.h

def cost_func(node):
    return node.risk

test_data = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581'
]

data = utils.get_day(2021, 15)
