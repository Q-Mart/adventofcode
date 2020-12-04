import utils
import re

forrest = utils.get_day(2020, 3)

example = ['..##.......',
           '#...#...#..',
           '.#....#..#.',
           '..#.#...#.#',
           '.#...##..#.',
           '..#.##.....',
           '.#.#.#....#',
           '.#........#',
           '#.##...#...',
           '#...##....#',
           '.#..#...#.#']

def path(forrest, right, down):
    current_row = 0
    current_col = 0
    trees = 0

    bottom = len(forrest) - 1
    width = len(forrest[0])

    while current_row != bottom:
        current_col += right
        current_col %= width
        current_row += down

        if forrest[current_row][current_col] == '#':
            trees += 1

    return trees

def r1d1(forrest):
    return path(forrest, 1, 1)

def r3d1(forrest):
    return path(forrest, 3, 1)

def r5d1(forrest):
    return path(forrest, 5, 1)

def r7d1(forrest):
    return path(forrest, 7, 1)

def r1d2(forrest):
    return path(forrest, 1, 2)

def multiply_all_paths(f):
    return r1d1(f) * r3d1(f) * r5d1(f) * r7d1(f) * r1d2(f)

assert(r3d1(example) == 7)
utils.print_part_1(r3d1(forrest))

assert(multiply_all_paths(example) == 336)
utils.print_part_2(multiply_all_paths(forrest))
