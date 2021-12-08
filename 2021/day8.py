import utils

orig_segments_to_digits = {
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

orig_digits_to_segments = {
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

def process(data):
    out = []
    for line in data:
        signals_str, values_str = line.split('|')
        out.append((signals_str.split(), values_str.split()))

    return out

def num_digits_with_unique_segments(values):
    unique_digit_lens = {
        len(orig_digits_to_segments[1]),
        len(orig_digits_to_segments[4]),
        len(orig_digits_to_segments[7]),
        len(orig_digits_to_segments[8])
    }

    result = [v for v in values if len(v) in unique_digit_lens]
    return len(result)

def total_num_digits_with_unque_segments(values_list):
    results = [num_digits_with_unique_segments(v) for v in values_list]
    return sum(results)

def deduce_output_values(signals, values):
    segments_to_digits = dict()
    digits_to_segments = dict()

    values = [frozenset(
        [d for d in v]
    ) for v in values]

    signals = [frozenset(
        [d for d in s]
    ) for s in signals]
    signals.sort(key=len)

    for sig in signals:
        # print(sig)
        # First work out 1, 4, 7 and 8
        if len(sig) == len(orig_digits_to_segments[1]):
            segments_to_digits[sig] = 1
            digits_to_segments[1] = sig
        elif len(sig) == len(orig_digits_to_segments[4]):
            segments_to_digits[sig] = 4
            digits_to_segments[4] = sig
        elif len(sig) == len(orig_digits_to_segments[7]):
            segments_to_digits[sig] = 7
            digits_to_segments[7] = sig
        elif len(sig) == len(orig_digits_to_segments[8]):
            segments_to_digits[sig] = 8
            digits_to_segments[8] = sig

        # Now work out 2, 3 and 5
        if len(sig) == 5:
            if digits_to_segments[1] < sig:
                segments_to_digits[sig] = 3
                digits_to_segments[3] = sig
            else:
                diff = sig - digits_to_segments[4]
                if len(diff) == 3:
                    segments_to_digits[sig] = 2
                    digits_to_segments[2] = sig
                else:
                    segments_to_digits[sig] = 5
                    digits_to_segments[5] = sig

        # Now work out 6, 9 and 0
        if len(sig) == 6:
            if digits_to_segments[5] < sig:
                if digits_to_segments[7] < sig:
                    segments_to_digits[sig] = 9
                    digits_to_segments[9] = sig
                else:
                    segments_to_digits[sig] = 6
                    digits_to_segments[6] = sig
            else:
                segments_to_digits[sig] = 0
                digits_to_segments[0] = sig

    result = ""
    for v in values:
        result += str(segments_to_digits[v])

    return int(result)

def total_outputs(sigval_pairs):
    r = 0
    for sig, val in sigval_pairs:
        r += deduce_output_values(sig, val)

    return r

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

test_values_2 = [val for signal, val in process(test_data_2)]
assert(total_num_digits_with_unque_segments(test_values_2) == 26)

values = [val for signal, val in process(data)]
utils.print_part_1(total_num_digits_with_unque_segments(values))

test_data_1 = process(test_data_1)
test_sigs_1 = test_data_1[0][0]
test_vals_1 = test_data_1[0][1]
assert(deduce_output_values(test_sigs_1, test_vals_1) == 5353)

test_data_2 = process(test_data_2)
assert(total_outputs(test_data_2) == 61229)

utils.print_part_2(total_outputs(process(data)))
