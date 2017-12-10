import math

INPUT = 312051

def manhattanDistance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def spiralRing(ringNo):
    highestVal = (ringNo)**2
    lowestVal = ((ringNo-2)**2) + 1

    locations = {}

    half = (ringNo-1) // 2
    possibleCoOrds = range(-half, half+1)
    size = len(possibleCoOrds)

    currentXIndex = size-1
    currentYIndex = 0
    direction = 'U'
    for i in range(highestVal, lowestVal, -1):
        locations[i] = (possibleCoOrds[currentXIndex], possibleCoOrds[currentYIndex])

        if currentYIndex == size-1 and currentXIndex == size-1:
            direction = 'L'
        elif currentYIndex == size-1 and currentXIndex == 0:
            direction = 'D'
        elif currentYIndex == 0 and currentXIndex == 0:
            direction = 'R'

        if direction == 'U': currentYIndex += 1
        elif direction == 'L': currentXIndex -= 1
        elif direction == 'D': currentYIndex -= 1
        elif direction == 'R': currentXIndex += 1
    return locations

def calcDistance(num):
    ringNumber = 1
    while ringNumber**2 < num:
        ringNumber += 2
    coords = spiralRing(ringNumber)[num]
    return manhattanDistance((0,0), coords)

assert calcDistance(12) == 3
assert calcDistance(23) == 2
assert calcDistance(1024) == 31
print(calcDistance(INPUT))

# used https://oeis.org/A141481/b141481.txt for part 2
