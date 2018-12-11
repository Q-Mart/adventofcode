import utils
import time

def getNumbers(data):
    return list(map(int, utils.getNumbers(data)))

def draw(board, positions):
    for y in range(len(board)):
        for x in range(len(board)):
            board[y][x] = ' '

    maxY = len(board) - 1
    maxX = len(board[0]) - 1
    for p in filter(lambda x: 0 <= x[0] <= maxX and 0 <= x[1] <= maxY, positions):
        board[p[1]][p[0]] = '#'

    for row in board:
        print (''.join(row))

def drawBoardAtTick(board, positions, velocities, t):
    for i in range(len(positions)):
        x, y = positions[i]
        vx, vy = velocities[i]

        positions[i] = (x+(vx*t), y+(vy*t))

    minX = min(map(lambda x: x[0], positions))
    minY = min(map(lambda x: x[1], positions))

    positions = list(map(lambda x: (x[0] - minX, x[1] - minY), positions))
    draw(board, positions)

def update(positions, velocities):
    for i in range(len(positions)):
        x, y = positions[i]
        vx, vy = velocities[i]

        positions[i] = (x+vx, y+vy)

rawData = utils.getDay(10)

data = list(map(getNumbers, rawData))

positions = []
velocities = []

for d in data:
    x, y, vx, vy = d
    positions.append((x, y))
    velocities.append((vx, vy))

# boxSizes = []
# for i in range(30000):
#     minX = min(positions[j][0] + i * velocities[j][0] for j in range(len(positions)))
#     maxX = max(positions[j][0] + i * velocities[j][0] for j in range(len(positions)))
#     minY = min(positions[j][1] + i * velocities[j][1] for j in range(len(positions)))
#     maxY = max(positions[j][1] + i * velocities[j][1] for j in range(len(positions)))

#     boxSizes.append(maxX-minX + maxY - minY)

# print (boxSizes.index(min(boxSizes)), min(boxSizes))

# The code above found that between 10036 had the smallest box size

board = [[' ' for i in range(100)] for j in range(100)]

drawBoardAtTick(board, positions, velocities, 10036)
