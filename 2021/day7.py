import utils
from collections import defaultdict

def to_positions(data):
    return list(
        map(
            int,
            data[0].split(',')
        )
    )

def fuel_to_align_to(final_pos, positions, fuel_func):
    s = 0
    for p in positions:
        diff = abs(final_pos-p)
        s += fuel_func(diff)

    return s

def fuel_to_most_efficient_pos(positions, fuel_func):
    fuel_needed = [
        fuel_to_align_to(pos,positions, fuel_func)
        for pos in range(min(positions), max(positions)+1)
    ]

    return min(fuel_needed)

positions = to_positions(utils.get_day(2021, 7))
test_positions = to_positions(['16,1,2,0,4,2,7,1,2,14'])

part_1_func = lambda d: d
assert(fuel_to_most_efficient_pos(test_positions, part_1_func) == 37)
utils.print_part_1(fuel_to_most_efficient_pos(positions, part_1_func))

part_2_func = lambda d: (d*(d+1))/2
assert(fuel_to_most_efficient_pos(test_positions, part_2_func) == 168)
utils.print_part_2(fuel_to_most_efficient_pos(positions, part_2_func))
