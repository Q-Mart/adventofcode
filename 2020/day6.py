import utils
from collections import defaultdict

answers = utils.get_day(2020, 6)

example1 = ['abcx',
            'abcy',
            'abcz']

example2 = ['abc',
            '',
            'a',
            'b',
            'c',
            '',
            'ab',
            'ac',
            '',
            'a',
            'a',
            'a',
            'a',
            '',
            'b']

def get_num_of_yes(answers):
    yes_answers = set()

    for a in answers:
        for letter in a:
            yes_answers.add(letter)

    return len(yes_answers)

def get_num_of_yes_that_all_answered(answers):
    num_people = len(answers)
    counter = defaultdict(int)

    for a in answers:
        for letter in a:
            counter[letter] += 1

    answers_that_all_answered_yes = 0
    for _, count in counter.items():
        if count == num_people:
            answers_that_all_answered_yes += 1

    return answers_that_all_answered_yes

def to_sublists(data):
    ret = []

    empty_count = data.count('')
    while empty_count != 0:
        sublist = []

        index = data.index('')
        sublist = data[:index]
        data = data[index+1:]

        ret.append(sublist)
        empty_count = data.count('')

    # Add last bit of unprocessed data
    ret.append(data)

    return ret

def process(data):
    total_yes_answers = 0

    data = to_sublists(data)

    for group in data:
        total_yes_answers += get_num_of_yes(group)

    return total_yes_answers

def process_all_answered_yes(data):
    total = 0

    data = to_sublists(data)

    for group in data:
        total += get_num_of_yes_that_all_answered(group)

    return total

assert(get_num_of_yes(example1) == 6)
assert(process(example2) == 11)

utils.print_part_1(process(answers))

assert(process_all_answered_yes(example2) == 6)
utils.print_part_2(process_all_answered_yes(answers))
