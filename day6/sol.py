numberLightsOn = 0
grid = []

for y in xrange(1000):
    grid.append([0]*1000)

class instruction():
    def __init__(self, type, x1, y1, x2, y2):
        self.type = type
        self.start_coords = (x1, y1)
        self.end_coords = (x2, y2)
        self.data = [self.type, self.start_coords, self.end_coords]

with open('input') as f:
    input = f.readlines()

#Compile instructions to be easier to handle
for i in xrange(len(input)):
    tokenized_input = input[i].strip().split()
    type = tokenized_input[0]

    if type == 'turn':
        #specify whether type is 'turn on' or 'turn off'
        type = tokenized_input[0] + tokenized_input[1]
        x1 = int(tokenized_input[2].split(',')[0])
        y1 = int(tokenized_input[2].split(',')[1])

        x2 = int(tokenized_input[4].split(',')[0])
        y2 = int(tokenized_input[4].split(',')[1])

        input[i] = instruction(type, x1, y1, x2, y2)

    else:
        x1 = int(tokenized_input[1].split(',')[0])
        y1 = int(tokenized_input[1].split(',')[1])

        x2 = int(tokenized_input[3].split(',')[0])
        y2 = int(tokenized_input[3].split(',')[1])

    input[i] = instruction(type, x1, y1, x2, y2)

#run instructions on grid
for instruction in input:
    for x in xrange(instruction.start_coords[0], instruction.end_coords[0] + 1):
        for y in xrange(instruction.start_coords[1], instruction.end_coords[1] + 1):
            if instruction.type == 'turnon': grid[x][y] = 1
            elif instruction.type == 'turnoff': grid[x][y] = 0
            else: grid[x][y] = not grid[x][y]

#check for lights that are on
for row in grid:
    for light in row:
        if light: numberLightsOn += 1

print numberLightsOn, 'lights are on'
