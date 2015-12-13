import itertools

#mapping of set of locations:distance
distanceTo = dict()
locations = set()
totalDistances = []

with open('input') as f:
    input = f.readlines()
    input = map(str.strip, input)

#tokenise input
for i in xrange(len(input)):
    input[i] = input[i].split(' = ')
    input[i][0] = input[i][0].split(' to ')

    distanceTo[tuple(input[i][0])] = int(input[i][1])
    input[i][0].reverse()
    distanceTo[tuple(input[i][0])] = int(input[i][1])

    locations.add(input[i][0][0])
    locations.add(input[i][0][1])

for path in itertools.permutations(list(locations)):
    pathDistance = 0
    for i in xrange(len(path) - 1):
        thisCity = path[i]
        nextCity = path[i + 1]
        pathDistance += distanceTo[thisCity, nextCity]

    totalDistances.append(pathDistance)

print min(totalDistances)
print max(totalDistances)
