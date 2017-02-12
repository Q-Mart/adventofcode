import re
import collections
import operator

def findBots(data, target):
    #Dict associates bot -> (low number dest, hight number dest)
    gives = {giver: (dest1, dest2)
             for (giver, dest1, dest2)
             in re.findall(r'(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', data)}

    #Dict associates bot/bin to values they contain
    values = collections.defaultdict(set)

    def give(source, chipNo, dest):
        values[source].discard(chipNo)
        values[dest].add(chipNo)

        chipsOfDest = values[dest]
        if chipsOfDest == target:
            print dest + ' has values ' + str(target)
        
        if len(chipsOfDest) == 2:
            give(dest, min(chipsOfDest), gives[dest][0])
            give(dest, max(chipsOfDest), gives[dest][1])

    for (chip, dest) in re.findall(r'value (\d+) goes to (\w+ \d+)', data):
        give('input bin', int(chip), dest)

    return values

with open('inputs/day10.txt') as f:
    data = f.read().strip()

values = findBots(data, {17, 61})

#Part 2
print values['output 0'].pop() * values['output 1'].pop() * values['output 2'].pop()
