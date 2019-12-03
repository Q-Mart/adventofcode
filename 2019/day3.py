import utils
# import pygame
# import sys

# BLACK = 0, 0, 0
# RED = 255, 0, 0,
# GREEN = 0, 255, 0,

# pygame.init()

data = utils.get_day(2019, 3)

def to_wire(line):
    return line.split(',')

def trace_pygame(wire, screen, col, dist):
    p1 = (100, 100)
    p2 = (100, 100)

    for direction in wire:
        last_x, last_y = p2
        orientation = direction[0]
        distance = int(direction[1:])

        for distance_one_point in range(1, distance+1):
            p1 = p2
            if orientation == 'U':
                p2 = (last_x, last_y+dist)
            elif orientation == 'D':
                p2 = (last_x, last_y-dist)
            elif orientation == 'R':
                p2 = (last_x+dist, last_y)
            elif orientation == 'L':
                p2 = (last_x-dist, last_y)

            pygame.draw.line(screen, col, p2, p1)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

def trace(wire):
    points = [(0,0)]

    for direction in wire:
        last_x, last_y = points[-1]
        orientation = direction[0]
        distance = int(direction[1:])

        for distance_one_point in range(1, distance+1):
            if orientation == 'U':
                points.append((last_x, last_y+distance_one_point))
            elif orientation == 'D':
                points.append((last_x, last_y-distance_one_point))
            elif orientation == 'R':
                points.append((last_x+distance_one_point, last_y))
            elif orientation == 'L':
                points.append((last_x-distance_one_point, last_y))

    return points

def find_intersections(wire_points_1, wire_points_2):
    wire_points_1 = set(wire_points_1)
    wire_points_2 = set(wire_points_2)

    return (wire_points_1 & wire_points_2) - {(0,0)}

def manhattan_distance(p1, p2=(0,0)):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def part_1(data):
    return min(
            map(manhattan_distance,
                find_intersections(trace(to_wire(data[0])), trace(to_wire(data[1])))
                )
            )

def part_2(data):
    points_1 = trace(to_wire(data[0]))
    points_2 = trace(to_wire(data[1]))

    combined_steps_for_each_intersection = []

    intersections = find_intersections(points_1, points_2)
    for intersection in intersections:
        combined_steps = 0
        for points in [points_1, points_2]:
            for point in points:
                if point == intersection:
                    break
                combined_steps += 1

        combined_steps_for_each_intersection.append(combined_steps)

    return min(combined_steps_for_each_intersection)

test_1 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72',
          'U62,R66,U55,R34,D71,R55,D58,R83']
assert(part_1(test_1) == 159)
test_2 = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
          'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
assert(part_1(test_2) == 135)

utils.print_part_1(part_1(data))

assert(part_2(test_1) == 610)
assert(part_2(test_2) == 410)

utils.print_part_2(part_2(data))

# size = width, height = 300, 300
# screen = pygame.display.set_mode(size)
# screen.fill(BLACK)

# trace_pygame(to_wire(data[0]), screen, RED, 5)
# trace_pygame(to_wire(data[1]), screen, GREEN, 5)
