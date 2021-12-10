import utils

closes = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

left_chars = '([{<'
right_chars = ')]}<'

def get_first_illegal_char(line):
    stack = []
    for char in line:
        if char in left_chars:
            stack.append(char)
        else:
            opener = stack.pop()
            if closes[opener] != char:
                return char, stack

    return None, stack

def syntax_score(char):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return points[char]

def score_corrupt_lines(data):
    result = []
    for line in data:
        c, _ = get_first_illegal_char(line)
        if c != None:
            result.append(syntax_score(c))

    return sum(result)

def autocomplete_score(completion_string, current_score=0):
    if completion_string == '':
        return current_score

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    char = completion_string[0]
    new_score = (5*current_score) + points[char]
    return autocomplete_score(completion_string[1:], new_score)

def get_completion_string(stack):
    completion_string = ''
    while stack != []:
        char = stack.pop()
        completion_string += closes[char]

    return completion_string

def get_incomplete_line_scores(data):
    scores = []

    for line in data:
        c, stack = get_first_illegal_char(line)
        if c != None:
            continue

        completion_string = get_completion_string(stack)
        scores.append(
            autocomplete_score(completion_string)
        )

    return scores

def get_middle_score(scores):
    scores = sorted(scores)

    # Length will always be odd, so middle index is (n-1)/2
    middle = int((len(scores)-1)/2)
    return scores[middle]

test = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]

data = utils.get_day(2021, 10)

assert score_corrupt_lines(test) == 26397
utils.print_part_1(score_corrupt_lines(data))

assert get_middle_score(get_incomplete_line_scores(test)) == 288957
utils.print_part_2(get_middle_score(get_incomplete_line_scores(data)))
