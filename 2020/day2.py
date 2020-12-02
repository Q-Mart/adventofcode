import utils
import re

db = utils.get_day(2020, 2)

example = ['1-3 a: abcde',
           '1-3 b: cdefg',
           '2-9 c: ccccccccc']

regex = re.compile('(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z])')

def extract_pw(db_line):
    return db_line.split(': ')[1]

def extract_occurence_rule(db_line):
    match = regex.match(db_line)
    ret = match.groupdict()

    for s in ['min', 'max']:
        ret[s] = int(ret[s])

    return ret

def is_valid_occurence(line):
    rule = extract_occurence_rule(line)
    pw = extract_pw(line)

    letter_count = pw.count(rule['letter'])

    if rule['min'] <= letter_count <= rule['max']:
        return True
    else:
        return False

def extract_locations_rule(db_line):
    ret = extract_occurence_rule(db_line)
    ret['pos_1'] = ret.pop('min') - 1
    ret['pos_2'] = ret.pop('max') - 1
    return ret

def is_valid_locations(line):
    rule = extract_locations_rule(line)
    pw = extract_pw(line)

    at_pos_1 = pw[rule['pos_1']] == rule['letter']
    at_pos_2 = pw[rule['pos_2']] == rule['letter']

    return at_pos_1 ^ at_pos_2

def count_valid_passwords(lines, valid_fn):
    c = 0
    for line in lines:
        if valid_fn(line):
            c += 1

    return c

assert(count_valid_passwords(example, is_valid_occurence) == 2)
assert(count_valid_passwords(example, is_valid_locations) == 1)

utils.print_part_1(count_valid_passwords(db, is_valid_occurence))
utils.print_part_2(count_valid_passwords(db, is_valid_locations))
