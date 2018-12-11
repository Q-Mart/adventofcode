import utils

GRID_LENGTH = 300

def powerLevel(x, y, serialNumber):
    rackID = x + 10
    power = rackID * y
    power += serialNumber
    power *= rackID

    if power < 100:
        power = 0
    else:
        power = int(str(power)[-3])

    power -= 5
    return power

def sumOfPowers(x, y, squareSize, grid):
    if x+squareSize-1 > GRID_LENGTH - 1 or y+squareSize-1 > GRID_LENGTH -1:
        return 0

    acc = 0
    for xi in range(x, x+squareSize):
        for yi in range(y, y+squareSize):
            acc += grid[yi][xi]

    return acc

serialNumber = int(utils.getDay(11)[0])

assert powerLevel(3,5,8) == 4
assert powerLevel(122,79,57) == -5
assert powerLevel(217,196,39) == 0
assert powerLevel(101,153,71) == 4

testGrid1 = [[-2,-4,4, 4, 4],
             [-4, 4,4, 4,-5],
             [4, 3,3, 4,-4],
             [1, 1,2, 4,-3],
             [-1, 0,2,-5,-2]]
assert(sumOfPowers(1,1,3,testGrid1) == 29)

grid = [[0 for i in range(GRID_LENGTH)] for j in range(GRID_LENGTH)]
for y in range(GRID_LENGTH):
    for x in range(GRID_LENGTH):
        grid[y][x] = powerLevel(x+1, y+1, serialNumber)

maxPower = 0
maxPowerIndex = (0, 0)
maxS = 0
for s in range(3, 21):
    for y in range(GRID_LENGTH):
        for x in range(GRID_LENGTH):
            p = sumOfPowers(x, y, s, grid)
            if p > maxPower:
                maxPower = p
                maxPowerIndex = (x+1, y+1)
                maxS = s
    print (s, maxPower, maxPowerIndex, maxS)

print (maxPower, maxPowerIndex, maxS)
