import utils

def template_and_rules(data):
    rules = {}
    for line in data[2:]:
        pair, insertion = line.split('->')
        pair = pair.strip()
        insertion = insertion.strip()
        rules[pair] = pair[0] + insertion + pair[1]

    return data[0], rules

def process(template, rules):
    print(rules)
    new_template = ''
    for i in range(len(template)):
        if i < len(template) - 1:
            template_slice = template[i:i+2]
            print(template_slice)
            if template_slice in rules:
                print(rules[template_slice])
                new_template += rules[template_slice]
            else:
                new_template += template_slice

    print(new_template)
    return new_template

def process_n_times(n, template, rules):
    temp = template
    for _ in range(n):
        temp = process(temp, rules)
    return temp


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
