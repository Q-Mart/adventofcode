import utils

def octopi(data):
    return [[int(c) for c in line] for line in data]

def step(octopi):

    def flash_surrounding(octopi, num_flashes=0):

        # Base case
        no_gt_9s = True
        for row in octopi:
            for octopus in row:
                if octopus > 9:
                    no_gt_9s = False

        if no_gt_9s:
            return num_flashes

        for y, row in enumerate(octopi):
            for x, octopus in enumerate(row):

                if octopus > 9:
                    octopi[y][x] = 0
                    num_flashes += 1

                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            # Pass over current octopus
                            if dy == 0 and dx == 0:
                                continue

                            if 0 <= y + dy < len(octopi):
                                if 0 <= x + dx < len(octopus):
                                    octopi[y+dy][x+dx] += 1


        return flash_surrounding(octopi, num_flashes)

def n_steps(octopi, n):
    total = 0
    for i in range(n):
        total += step(octopi)

    return total

test = octopi([
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526'
])

data = octopi(utils.get_day(2021, 11))

print(n_steps(test, 10))
