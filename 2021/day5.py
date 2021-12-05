import utils
from collections import defaultdict, namedtuple

data = utils.get_day(2021, 5)

test_data = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]

Point = namedtuple('Point', ['x', 'y'])

def data_to_vent_coords(data):
    coords = []

    def to_coord_tuple(p):
        split = p.split(',')
        return Point(int(split[0]), int(split[1]))

    for p1, _, p2 in list(map(str.split, data)):
        coords.append(
            (to_coord_tuple(p1), to_coord_tuple(p2))
        )

    return coords

def same_xs(p1, p2):
    return p1.x == p2.x

def same_ys(p1, p2):
    return p1.y == p2.y

def is_line_straight(p1, p2):
    return same_xs(p1, p2) or same_ys(p1, p2)

def num_overlapping_points(coords, guard_f):
    points_covered = defaultdict(int)

    for p1, p2 in coords:
        if guard_f(p1, p2):

            finished = False
            current_p = p1
            while not finished:
                points_covered[current_p] += 1

                if same_xs(current_p, p2) and same_ys(current_p, p2):
                    finished = True

                if not same_xs(current_p, p2):
                    if p2.x > current_p.x:
                        current_p = Point(current_p.x+1, current_p.y)
                    else:
                        current_p = Point(current_p.x-1, current_p.y)

                if not same_ys(current_p, p2):
                    if p2.y > current_p.y:
                        current_p = Point(current_p.x, current_p.y+1)
                    else:
                        current_p = Point(current_p.x, current_p.y-1)

    total_overlapping_points = 0
    for k, number_of_vents in points_covered.items():
        if number_of_vents > 1:
            total_overlapping_points += 1

    return total_overlapping_points

coords = data_to_vent_coords(data)
test_coords = data_to_vent_coords(test_data)

assert(num_overlapping_points(test_coords, is_line_straight) == 5)
utils.print_part_1(num_overlapping_points(coords, is_line_straight))

assert(num_overlapping_points(test_coords, lambda a, b: True) == 12)
utils.print_part_2(num_overlapping_points(coords, lambda a, b: True))
