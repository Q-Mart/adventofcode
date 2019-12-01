import utils
import string

def adjacentOfOppositePolarity(x,y):
    if abs(ord(x) - ord(y)) == 32:
        return True
    else:
        return False

def react(polymer):
    result = ''
    for c in polymer:
        if result and adjacentOfOppositePolarity(c, result[-1]):
            result = result[:len(result)-1]
        else:
            result += c

    return result

polymer = utils.getDay(5)[0]
# polymer = "dabAcCaCBAcCcaDA"

def part1():
    print (len(react(polymer)))

def part2():
    smallestLength = react(polymer)
    smallestLetter = None

    for c in string.ascii_lowercase:
        length = len(react(str(filter(lambda x: x != c and x != c.upper(), polymer))))

        if length < smallestLength:
            smallestLength = length
            smallestLetter = c

    print (smallestLetter, smallestLength)

part1()
part2()
