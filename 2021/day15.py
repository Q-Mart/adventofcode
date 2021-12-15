import utils
from collections import namedtuple

Node = namedtuple('Node', ['risk', 'h', 'x', 'y'])

def to_grid(data):
    max_y = len(data) - 1
    max_x = len(data[0]) - 1

    grid = []
    for y, line in enumerate(data):
        row = []
        for x, c in enumerate(line):
            row.append(
                Node(
                    int(c),
                    (max_x - x) + (max_y - y),
                    x,
                    y
                )
            )

        grid.append(row)

    return grid

def h_func(node):
    return node.h

def cost_func(node):
    return node.risk

def moves_func(node, grid):
    next_nodes = []

    for dy in [-1, 1]:
            if 0 <= node.y + dy < len(grid):
                next_nodes.append(grid[node.y+dy][node.x])

    for dx in [-1, 1]:
            if 0 <= node.x + dx < len(grid[0]):
                next_nodes.append(grid[node.y][node.x+dx])

    return next_nodes

def get_risk_start_not_entered(path):
    return sum([s.risk for s in path[1:]])

def gen_5x5_grid(data):
    new_data = []

    def wraparound(val):
        if val > 9:
            return val % 9
        return val

    # Create the first row of tiles
    for row in data:
        new_row = ''
        for i in range(5):
            tile = [int(c) for c in row]
            new_row += ''.join([str((wraparound(t + i))) for t in tile])

        new_data.append(''.join(new_row))

    height = len(data)
    # Now the new first row is done, replicate it in the y direction 4 times
    rows = new_data[0: height]
    for i in range(4):
        for row in rows:
            tile = [int(c) for c in row]
            new_row = ''.join([str(wraparound(t + i + 1)) for t in tile])
            new_data.append(new_row)

    return to_grid(new_data)

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

test_grid = to_grid(test_data)
moves_func_test_grid = lambda s: moves_func(s, test_grid)
test_path = utils.a_star(test_grid[0][0], h_func, cost_func, moves_func_test_grid)
assert get_risk_start_not_entered(test_path) == 40

grid = to_grid(data)
moves_func_part_1 = lambda s: moves_func(s, grid)
path = utils.a_star(grid[0][0], h_func, cost_func, moves_func_part_1)
utils.print_part_1(get_risk_start_not_entered(path))

test_grid = gen_5x5_grid(test_data)
moves_func_test_grid = lambda s: moves_func(s, test_grid)
test_path = utils.a_star(test_grid[0][0], h_func, cost_func, moves_func_test_grid)
assert get_risk_start_not_entered(test_path) == 315

grid = gen_5x5_grid(data)
moves_func_part_1 = lambda s: moves_func(s, grid)
path = utils.a_star(grid[0][0], h_func, cost_func, moves_func_part_1)
utils.print_part_2(get_risk_start_not_entered(path))
