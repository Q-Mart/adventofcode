import utils

def to_heightmap(data):
    return [
        [int(c) for c in line]
        for line in data
    ]

data = to_heightmap(utils.get_day(2021, 9))

test = to_heightmap(
    [
        '2199943210',
        '3987894921',
        '9856789892',
        '8767896789',
        '9899965678'
    ]
)

def get_low_point_coords(hm):
    coords = []
    for y, row in enumerate(hm):
        for x, point in enumerate(row):

            lower_than_top_and_bottom = True
            for dy in [-1, 1]:
                if 0 <= y+dy < len(hm):
                    if hm[y][x] >= hm[y+dy][x]:
                        lower_than_top_and_bottom = False

            lower_than_left_and_right = True
            for dx in [-1, 1]:
                if 0 <= x+dx < len(hm[0]):
                    if hm[y][x] >= hm[y][x+dx]:
                        lower_than_left_and_right = False

            if lower_than_left_and_right and lower_than_top_and_bottom:
                coords.append((x, y))

    return coords

def total_risk_levels(hm, low_points):
    risk_levels = [hm[y][x] + 1 for x, y in low_points]
    return sum(risk_levels)

def get_basin_size(hm, start):

    size = 0
    visited = []

    def recurse(current_point):
        nonlocal size
        nonlocal visited

        visited.append(current_point)

        x, y = current_point

        # Base case
        if hm[y][x] == 9:
            return size

        # Include the current point in the basin size
        size += 1

        for dy in [-1, 1]:
            if 0 <= y+dy < len(hm) and (x, y+dy) not in visited:
                recurse((x, y+dy))

        for dx in [-1, 1]:
            if 0 <= x+dx < len(hm[0]) and (x+dx, y) not in visited:
                recurse((x+dx, y))

    recurse(start)
    return size

def part1(hm):
    return total_risk_levels(hm, get_low_point_coords(hm))

def part2(hm):
    basin_sizes = []

    points = get_low_point_coords(hm)
    for point in points:
        basin_sizes.append(get_basin_size(hm, point))

    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

assert part1(test) == 15
utils.print_part_1(part1(data))

assert part2(test) == 1134
utils.print_part_2(part2(data))
