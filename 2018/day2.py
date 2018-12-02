import utils
import collections

boxIDs = utils.getDay(2)

def part1():
    twoLetters = 0
    threeLetters = 0

    for iD in boxIDs:
        counter = collections.Counter(iD)
        if 3 in counter.values(): threeLetters += 1
        if 2 in counter.values(): twoLetters += 1

    result = twoLetters * threeLetters
    return result

def part2():
    for id1 in boxIDs:
        for id2 in boxIDs:
            zipped = zip(id1, id2)
            diffLetters = list(filter(lambda x: x[0] != x[1], zipped))
            if len(diffLetters) == 1:
                sameLetters = filter(lambda x: x[0] == x[1], zip(id1, id2))
                sameLetters = ''.join(map(lambda x: x[0], sameLetters))
                return sameLetters

print (part1())
print (part2())
