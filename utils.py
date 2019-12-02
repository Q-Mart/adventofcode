def get_day(year, day_number):
    lines = []
    with open("{0}/inputs/{1}.txt".format(year, day_number)) as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))
    return lines

def print_part_1(ans):
    print('{0}Part 1: {1}{2}'.format('\033[91m', ans, '\033[0m'))

def print_part_2(ans):
    print('{0}Part 2: {1}{2}'.format('\033[92m', ans, '\033[0m'))
