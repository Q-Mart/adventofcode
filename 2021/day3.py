import utils
from collections import defaultdict

data = utils.get_day(2021, 3)

def _generate_number_by_applying_f_to_transposed_bitlist(data, f):
    digit_counter = defaultdict(list)
    for d in data:
        l = []
        for i, digit in enumerate(d):
            digit_counter[i].append(digit)

    result = ""
    for i in range(len(data[0])):
        result += f(digit_counter[i])

    return int(result, 2)

def gamma(data):
    f = lambda l: max(set(l), key=l.count)
    return _generate_number_by_applying_f_to_transposed_bitlist(data, f)

def epsilon(data):
    f = lambda l: min(set(l), key=l.count)
    return _generate_number_by_applying_f_to_transposed_bitlist(data, f)

def _generate_number_from_bit_criteria(data, criteria_func):
    def get_column(data, i):
        l = []
        for d in data:
            l += d[i]
        return l

    r = data
    for i in range(len(data[0])):
        c = criteria_func(get_column(r, i))

        if len(r) == 1:
            break

        r = [x for x in r if x[i] == c]

    if (len(r) != 1):
        raise Exception(f'List {r} is not of length 1')

    return int(r[0], 2)

def oxygen_gen_rating(data):
    def criteria_func(l):
        ones = l.count("1")
        zeroes = l.count("0")

        if ones >= zeroes:
            return "1"
        else:
            return "0"

    return _generate_number_from_bit_criteria(data, criteria_func)

def c02_scrub_rating(data):
    def criteria_func(l):
        ones = l.count("1")
        zeroes = l.count("0")

        if ones < zeroes:
            return "1"
        else:
            return "0"

    return _generate_number_from_bit_criteria(data, criteria_func)

test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

assert(gamma(test_data) == 22)
assert(epsilon(test_data) == 9)
utils.print_part_1(gamma(data) * epsilon(data))

assert(oxygen_gen_rating(test_data) == 23)
assert(c02_scrub_rating(test_data) == 10)
utils.print_part_2(oxygen_gen_rating(data) * c02_scrub_rating(data))
