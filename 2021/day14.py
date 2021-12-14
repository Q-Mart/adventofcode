import utils
import sys
from collections import defaultdict

def template_and_rules(data):
    rules = {}
    for line in data[2:]:
        pair, insertion = line.split('->')
        pair = pair.strip()
        insertion = insertion.strip()
        rules[pair] = pair[0] + insertion + pair[1]

    return data[0], rules

def process(template, rules):
    i = 0
    while i < len(template):
        template_slice = template[i:i+2]
        if template_slice in rules:
            template = template[:i] + rules[template_slice] + template[i+2:]
            i += 2
        else:
            i += 1

    return template

def process_n_times(n, template, rules):
    temp = template
    for _ in range(n):
        temp = process(temp, rules)
    return temp

def new_process_n_times(n, template, rules):
    pairs = defaultdict(int)
    counts = defaultdict(int)

    # Populate counts dict
    for c in template:
        counts[c] = template.count(c)

    #Populate pairs dict
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pairs[pair] += 1

    for i in range(n):
        new_pairs = defaultdict(int)
        for pair, population in pairs.items():
            if pair in rules:
                child_1, child_2 = rules[pair][:2], rules[pair][1:]
                new_pairs[child_1] += population
                new_pairs[child_2] += population

                counts[rules[pair][1]] += population
            else:
                new_pairs[pair] = population

        pairs = new_pairs

    return counts

def max_and_min_chars(template):
    max = 0
    min = sys.maxsize
    for char in template:
        c = template.count(char)
        if c > max:
            max = c
        if c < min:
            min = c

    return max, min

def most_common_minus_least_common_after_n_processes(n, data):
    template_after_n = process_n_times(n, *template_and_rules(data))
    max, min = max_and_min_chars(template_after_n)
    return max - min

def fast_most_common_minus_least_common_after_n_process(n, data):
    counts = new_process_n_times(n, *template_and_rules(data))
    return max(counts.values()) - min(counts.values())

test_data = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C'
]

data = utils.get_day(2021, 14)

assert process(*template_and_rules(test_data)) == 'NCNBCHB'
assert process_n_times(2, *template_and_rules(test_data)) == 'NBCCNBBBCBHCB'
assert process_n_times(3, *template_and_rules(test_data)) == 'NBBBCNCCNBBNBNBBCHBHHBCHB'
assert process_n_times(4, *template_and_rules(test_data)) == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
assert len(process_n_times(5, *template_and_rules(test_data))) == 97
assert len(process_n_times(10, *template_and_rules(test_data))) == 3073

assert most_common_minus_least_common_after_n_processes(10, test_data) == 1588
utils.print_part_1(most_common_minus_least_common_after_n_processes(10, data))

assert fast_most_common_minus_least_common_after_n_process(10, test_data) == 1588
assert fast_most_common_minus_least_common_after_n_process(40, test_data) == 2188189693529
