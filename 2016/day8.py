import itertools, urwid

WIDTH = 50
LENGTH = 6

grid = [[False]*WIDTH for _ in xrange(LENGTH)]

def rect(a, b, grid):
    for x ,y in itertools.product(xrange(a), xrange(b)):
        grid[y][x] = True
    return grid

def rotate_row(a, b, grid):
    row = grid[a]
    
    for _ in xrange(b):
        temp = row.pop()
        row = [temp] + row

    grid[a] = row
    return grid

def rotate_col(a, b, grid):
    col = []
    for y in xrange(LENGTH):
        col.append(grid[y][a])

    for _ in xrange(b):
        temp = col.pop()
        col = [temp] + col

    for y in xrange(LENGTH):
        grid[y][a] = col[y]

    return grid

def draw(grid):
    string = ""
    for row in grid:
        for element in row:
            if element:
                string += '#'
            else:
                string += '.'

        string += '\n'

    print string

def process(instruction, grid):
    tokens = instruction.split()

    if tokens[0] == 'rect':
        a, b = map(int, tokens[1].split('x'))
        return rect(a,b, grid)

    else:
        a = int(tokens[2][2:])
        b = int(tokens[4])
        if tokens[1] == 'column': return rotate_col(a, b, grid)
        else: return rotate_row(a, b, grid)

with open('inputs/day8.txt') as f:
    data = map(str.strip, f.readlines())

for instruction in data:
    grid = process(instruction, grid)
    draw(grid)

print sum(map(sum, grid))
