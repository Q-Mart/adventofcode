import collections

def correct(message):
    mostCommon =  collections.Counter(message).most_common()
    mostCommon.reverse()
    return mostCommon[0][0]

def transpose(matrix):
    return zip(*matrix)

with open('inputs/day6.txt') as f:
    data = f.readlines()

data = transpose([list(l.strip()) for l in data])

message = ''
for column in data:
    message += correct(column)

print message
