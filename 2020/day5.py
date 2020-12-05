import utils
import math

boarding_passes = utils.get_day(2020, 5)

example1 = 'FBFBBFFRLR'
example2 = 'BFFFBBFRRR'
example3 = 'FFFBBBFRRR'
example4 = 'BBFFBBFRLL'

def binary_search(instructions, min, max, descision_f):
    for i in instructions:
        mid = math.floor((max - min)/2) + min
        current = mid

        if descision_f(i):
            max = mid
            current = min
        else:
            min = mid + 1
            current = max

    return current

def get_row(b_pass):
    return binary_search(b_pass[0:7], 0, 127, lambda i: i == 'F')

def get_col(b_pass):
    return binary_search(b_pass[-3:], 0, 7, lambda i: i == 'L')

def seat_id(b_pass):
    row = get_row(b_pass)
    col = get_col(b_pass)
    return (row * 8) + col

assert(seat_id(example1) == 357)
assert(seat_id(example2) == 567)
assert(seat_id(example3) == 119)
assert(seat_id(example4) == 820)

utils.print_part_1(max(map(seat_id, boarding_passes)))

ids = sorted(map(seat_id, boarding_passes))

for i, id in enumerate(ids):
    # ignore very start and end
    if i >= 2 and i <= len(ids) - 2:
        one_before = ids[i-1]
        if one_before != id - 1:
            utils.print_part_2(id-1)
            break
