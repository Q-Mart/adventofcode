import utils
import re

pp_data = utils.get_day(2020, 4)

example = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
           'byr:1937 iyr:2017 cid:147 hgt:183cm',
           '',
           'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
           'hcl:#cfa07d byr:1929',
           '',
           'hcl:#ae17e1 iyr:2013',
           'eyr:2024',
           'ecl:brn pid:760753108 byr:1931',
           'hgt:179cm',
           '',
           'hcl:#cfa07d eyr:2025 pid:166559648',
           'iyr:2011 ecl:brn hgt:59in']

hcl_regex = re.compile('#(\d|[a-f]){6}')
pid_regex = re.compile('^\d{9}$')

VALID_KEYS = ['byr',
              'iyr',
              'eyr',
              'hgt',
              'hcl',
              'ecl',
              'pid']

def to_dict(string):
    no_spaces = string.split()
    kvs = list(map(lambda x: tuple(x.split(':')), no_spaces))
    return dict(kvs)

def is_valid(passport):
    for key in VALID_KEYS:
        if key not in passport:
            return False

    return True

def is_valid_stronger_rules(passport):
    if not is_valid(passport):
        return False

    if not(1920 <= int(passport['byr']) <= 2002):
        return False

    if not(2010 <= int(passport['iyr']) <= 2020):
        return False

    if not(2020 <= int(passport['eyr']) <= 2030):
        return False

    unit = passport['hgt'][-2:]
    if unit not in ['cm', 'in']:
        return False
    else:
        height = int(passport['hgt'][:-2])
        if unit == 'cm' and not(150 <= height <= 193):
            return False
        elif unit == 'in' and not(59 <= height <= 76):
            return False

    if hcl_regex.match(passport['hcl']) == None:
        return False

    cols = ['amb', 'blu', 'brn', 'gry',
            'grn', 'hzl', 'oth']
    if passport['ecl'] not in cols:
        return False

    if pid_regex.match(passport['pid']) == None:
        return False

    return True

def process(data):
    valid_passports = 0
    stronger_valid_passports = 0

    acc = ''
    for i, line in enumerate(data):
        if line == '' or (i == len(data)-1 and acc != ''):
            acc = acc[1:]

            passport = to_dict(acc)
            if is_valid(passport):
                valid_passports += 1

            if is_valid_stronger_rules(passport):
                stronger_valid_passports += 1

            acc = ''
        elif i == len(data)-1 and acc == '':
            passport = to_dict(line)
            if is_valid(passport):
                valid_passports += 1

            if is_valid_stronger_rules(passport):
                stronger_valid_passports += 1
        else:
            acc += ' ' + line

    return valid_passports, stronger_valid_passports

assert(process(example)[0] == 2)
utils.print_part_1(process(pp_data)[0])

all_invalid = ['eyr:1972 cid:100',
               'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
               '',
               'iyr:2019',
               'hcl:#602927 eyr:1967 hgt:170cm',
               'ecl:grn pid:012533040 byr:1946',
               '',
               'hcl:dab227 iyr:2012',
               'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
               '',
               'hgt:59cm ecl:zzz',
               'eyr:2038 hcl:74454a iyr:2023',
               'pid:3556412378 byr:2007']
assert(process(all_invalid)[1] == 0)

all_valid = ['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
             'hcl:#623a2f',
             '',
             'eyr:2029 ecl:blu cid:129 byr:1989',
             'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
             '',
             'hcl:#888785',
             'hgt:164cm byr:2001 iyr:2015 cid:88',
             'pid:545766238 ecl:hzl',
             'eyr:2022',
             '',
             'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']
assert(process(all_valid)[1] == 4)
utils.print_part_2(process(pp_data)[1])
