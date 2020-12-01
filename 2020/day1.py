import utils
import itertools

entries = list(map(int, utils.get_day(2020, 1)))

for a, b in itertools.combinations(entries, 2):
    if a + b == 2020:
        utils.print_part_1(a*b)
        break

for a, b, c in itertools.combinations(entries, 3):
    if a + b + c == 2020:
        utils.print_part_2(a*b*c)
        break
