import utils

data = utils.get_day(2019, 1)

def fuel_for(mass):
    x = int(mass/3) - 2
    return 0 if x < 0 else x

def fuel_for_including_fuel(mass):
    total_fuel_required = 0
    fuel_to_add = fuel_for(mass)
    while fuel_to_add != 0:
        total_fuel_required += fuel_to_add
        fuel_to_add = fuel_for(fuel_to_add)

    return total_fuel_required

utils.print_part_1(sum(map(lambda x: fuel_for(int(x)), data)))

assert(fuel_for_including_fuel(14) == 2)
assert(fuel_for_including_fuel(1969) == 966)
assert(fuel_for_including_fuel(100756) == 50346)

utils.print_part_2(sum(map(lambda x: fuel_for_including_fuel(int(x)), data)))
