#Solution inspired by Peter Norvig
import re

def decompress(seq):
    result = ''
    i = 0
    seq = seq.replace(' ', '') #remove whitespace
    regex = re.compile(r'\((\d+)x(\d+)\)').match
    while i < len(seq):
        match = regex(seq, i)

        if match:
            i = match.end()
            numberOfChars, numberOfRepititions = map(int, match.groups())
            result += seq[i:i+numberOfChars] * numberOfRepititions
            i += numberOfChars

        else:
            result += seq[i]
            i += 1

    return result

def decompress2(seq):
    length = 0
    i = 0
    seq = seq.replace(' ', '') #remove whitespace
    regex = re.compile(r'\((\d+)x(\d+)\)').match
    while i < len(seq):
        match = regex(seq, i)

        if match:
            numberOfChars, numberOfRepititions = map(int, match.groups())
            i = match.end(0)
            length += numberOfRepititions * decompress2(seq[i:i+numberOfChars])
            i += numberOfChars

        else:
            length += 1
            i += 1


    return length

assert len(decompress('A(1x5)BC')) == 7
assert len(decompress('(3x3)XYZ')) == 9
assert len(decompress('A(2x2)BCD(2x2)EFG')) == 11
assert len(decompress('(6x1)(1x3)A')) == 6
assert len(decompress('X(8x2)(3x3)ABCY')) == 18

assert decompress2('X(8x2)(3x3)ABCY') == 20
assert decompress2('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
assert decompress2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') == 445

with open('inputs/day9.txt') as f:
    data = f.read().strip()

print len(decompress(data))
print decompress2(data)
