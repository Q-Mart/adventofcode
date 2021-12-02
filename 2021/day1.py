import utils
import itertools

depths = list(map(int, utils.get_day(2021, 1)))

def num_increasing_depths(ds):
    s = 0
    for i in range(len(ds)-1):
        if ds[i] < ds[i+1]:
            s+=1

    return s

def three_measurement_window(ds):
    return [ds[i] + ds[i+1] + ds[i+2] for i in range(len(ds)-2)]

test_1 = [199,200,208,210,200,207,240,269,260,263]

assert(num_increasing_depths(test_1) == 7)
utils.print_part_1(num_increasing_depths(depths))

assert(num_increasing_depths(three_measurement_window(test_1)) == 5)
utils.print_part_2(num_increasing_depths(three_measurement_window(depths)))
