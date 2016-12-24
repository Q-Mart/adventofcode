class Explorer():
    
    def __init__(self):
        self.POSITIONS = ('N', 'E', 'S', 'W')
        self.positionPtr = 0
        self.x = 0
        self.y = 0
        self.xTravelled = 0
        self.yTravelled = 0
        self.visitedLocations = set()
        self.foundFactory = False

    def turnLeft(self):
        self.positionPtr -= 1
        return self.positionPtr

    def turnRight(self):
        self.positionPtr = (self.positionPtr + 1) % 4
        return self.positionPtr

    def turn(self, direction):
        if direction == 'R': return self.turnRight()
        else: return self.turnLeft()

    def walk(self, num):
        if self.foundFactory: return

        position = self.POSITIONS[self.positionPtr]

        for i in xrange(num):
            if position == 'N': self.yTravelled += 1
            elif position == 'S': self.yTravelled -= 1
            elif position == 'E': self.xTravelled += 1
            elif position == 'W': self.xTravelled -= 1

            currentLocation = (self.xTravelled, self.yTravelled)
            if currentLocation in self.visitedLocations:
                self.foundFactory = True
                break

            self.visitedLocations.add(currentLocation)

    def processToken(self, token):
        if self.foundFactory: return

        direction = token[0]
        distance = int(token[1:])

        self.turn(direction)
        self.walk(distance)

    def getTotalDistanceTravelled(self):
        return abs(self.xTravelled) + abs(self.yTravelled)

with open('inputs/day1.txt') as f:
    data = f.readline()

tokens =  map(str.strip, data.split(','))

explorer = Explorer()
map(explorer.processToken, tokens)
print explorer.getTotalDistanceTravelled()
