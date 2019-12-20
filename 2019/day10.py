import utils

data = utils.get_day(2019, 10)

def gradient_pair(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def get_locations_of_asteroids(field):
    locations = set()

    max_y = len(field)
    max_x = len(field[0])
    for y in range(max_y):
        for x in range(max_x):
            if field[y][x] == '#':
                locations |= {(x, y)}

    return locations

def find_best_location(field):
    #x, y, number of asteroids
    best = (0, 0, 0)

    locations = get_locations_of_asteroids(field)
    for asteroid in locations:
        gradients = set()
        others = locations - {asteroid}
        for other in others:
            gradients |= {gradient(asteroid[0], asteroid[1], other[0], other[1])}

        if len(gradients) > best[2]:
            best = (asteroid[0], asteroid[1], len(gradients))

    return best

test_1 = ['.#..#',
          '.....',
          '#####',
          '....#',
          '...##']
print(find_best_location(test_1))

test_2 = ['......#.#.',
          '#..#.#....',
          '..#######.',
          '.#.#.###..',
          '.#..#.....',
          '..#....#.#',
          '#..#....#.',
          '.##.#..###',
          '##...#..#.',
          '.#....####']
print(find_best_location(test_2))

test_3 = ['#.#...#.#.',
          '.###....#.',
          '.#....#...',
          '##.#.#.#.#',
          '....#.#.#.',
          '.##..###.#',
          '..#...##..',
          '..##....##',
          '......#...',
          '.####.###.']
print(find_best_location(test_3))
