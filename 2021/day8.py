import utils

segments_to_digits = {
    frozenset(['a', 'b', 'c', 'e', 'f', 'g']) : 0,
    frozenset(['c', 'f']): 1,
    frozenset(['a', 'c', 'd', 'e', 'g']): 2,
    frozenset(['a', 'c', 'd', 'f', 'g']): 3,
    frozenset(['b', 'c', 'd', 'f']): 4,
    frozenset(['a', 'b', 'd', 'f', 'g']): 5,
    frozenset(['a', 'b', 'd', 'e', 'f', 'g']): 6,
    frozenset(['a', 'c', 'f']): 7,
    frozenset(['a', 'b', 'c', 'd', 'e', 'f', 'g']) : 8,
    frozenset(['a', 'b', 'c', 'd', 'f', 'g']) : 9,
}

digits_to_segments = {
    0: frozenset(['a', 'b', 'c', 'e', 'f', 'g']),
    1: frozenset(['c', 'f']),
    2: frozenset(['a', 'c', 'd', 'e', 'g']),
    3: frozenset(['a', 'c', 'd', 'f', 'g']),
    4: frozenset(['b', 'c', 'd', 'f']),
    5: frozenset(['a', 'b', 'd', 'f', 'g']),
    6: frozenset(['a', 'b', 'd', 'e', 'f', 'g']),
    7: frozenset(['a', 'c', 'f']),
    8: frozenset(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
    9: frozenset(['a', 'b', 'c', 'd', 'f', 'g']),
}

def get_output_values(data):
    values = []
    for line in data:
        values_str = line.split('|')[1]
        values.append(values_str.split())

    return values

def num_digits_with_unique_segments(values):
    unique_digit_lens = {
        len(digits_to_segments[1]),
        len(digits_to_segments[4]),
        len(digits_to_segments[7]),
        len(digits_to_segments[8])
    }

    result = [v for v in values if len(v) in unique_digit_lens]
    return len(result)

def total_num_digits_with_unque_segments(values_list):
    results = [num_digits_with_unique_segments(v) for v in values_list]
    return sum(results)

data = utils.get_day(2021, 8)

test_data_1 = [
    'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
]

test_data_2 = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'
]

assert(total_num_digits_with_unque_segments(get_output_values(test_data_2)) == 26)
utils.print_part_1(total_num_digits_with_unque_segments(get_output_values(data)))
