import utils

# Puzzle input
START = 278384
END = 824795

def to_list_of_digits(num):
    return [int(x) for x in str(num)]

def has_two_adjacent_digits(num_list):
    result = False
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1]:
            result = True

    return result

def has_two_but_not_more_adjacent_digits(num_list):
    result = False

    i = 0
    while i < len(num_list):
        current_digit = num_list[i]

        num_adjacent = 0
        while num_list[i] == current_digit:
            num_adjacent += 1
            i += 1

            if i == len(num_list):
                break

        if num_adjacent == 2:
            result = True

    return result

def digits_never_decrease(num_list):
    result = True
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            result = False

    return result

def criteria(password):
    password_digits = to_list_of_digits(password)
    return has_two_adjacent_digits(password_digits) and digits_never_decrease(password_digits)

def criteria_part_2(password):
    password_digits = to_list_of_digits(password)
    return has_two_but_not_more_adjacent_digits(password_digits) and digits_never_decrease(password_digits)

assert(criteria(111111) == True)
assert(criteria(223450) == False)
assert(criteria(123789) == False)

passwords = set()
for i in range(START, END+1):
    if criteria(i):
        passwords |= {i}

utils.print_part_1(len(passwords))

assert(criteria_part_2(112233) == True)
assert(criteria_part_2(123444) == False)
assert(criteria_part_2(111122) == True)
assert(criteria_part_2(111111) == False)

passwords = set()
for i in range(START, END+1):
    if criteria_part_2(i):
        passwords |= {i}

utils.print_part_2(len(passwords))
