import utils
import math

data = utils.get_day(2019, 10)

def get_x(theta, h_length):
    return h_length * math.sin(theta)

def get_y(theta, h_length):
    return h_length * math.cos(theta)

def check_for_asteroid(x, y, field):
    if x.is_integer() and y.is_integer():
        return field[round(y)][round(x)] == '#'
    else:
        return False

def at_edge(x, y, field):
    max_y = len(field)
    max_x = len(field[0])
    if (0 <= x < max_x) and (0 <= y < max_y):
        return False
    else:
        return True

def scan_for_asteroids(asteroid_x, asteroid_y, field):
    visited_asteroids = {(asteroid_x, asteroid_y)}
    for theta in range(360):
        found_asteroid = False
        hit_edge = False
        h_length = 1
        while not (found_asteroid or hit_edge):
            if 0 <= theta <= 90:
                new_x = asteroid_x - get_x(theta, h_length)
                new_y = asteroid_y - get_y(theta, h_length)
            elif 90 < theta <= 180:
                new_x = asteroid_x + get_x(theta, h_length)
                new_y = asteroid_y - get_y(theta, h_length)
            elif 180 < theta <= 270:
                new_x = asteroid_x + get_x(theta, h_length)
                new_y = asteroid_y + get_y(theta, h_length)
            elif 270 < theta <= 360:
                new_x = asteroid_x - get_x(theta, h_length)
                new_y = asteroid_y + get_y(theta, h_length)

            hit_edge = at_edge(new_x, new_y, field)
            if hit_edge:
                break

            found_asteroid = check_for_asteroid(new_x, new_y, field)
            if found_asteroid:
                visited_asteroids |= {(new_x, new_y)}
                break

            h_length += 1

    return len(visited_asteroids)

def find_best_location(field):
    #x, y, number of asteroids
    best = (0, 0, 0)

    max_y = len(field)
    max_x = len(field[0])
    for y in range(max_y):
        for x in range(max_x):
            if field[y][x] == '#':
                number_of_asteroids = scan_for_asteroids(x, y, field)
                if number_of_asteroids > best[2]:
                    best = (x, y, number_of_asteroids)

    return best

test_1 = ['.#..#',
          '.....',
          '#####',
          '....#',
          '...##']
print(find_best_location(test_1))
