END_TIME = 2503
reindeers = dict()

class reindeer():
    def __init__(self, speed, travelTime, restTime):

        self.speed = speed
        self.totalTravelTime = travelTime
        self.totalRestTime = restTime

        self.points = 0
        self.distance = 0
        self.travelTime = 0
        self.restTime = 0
        self.isTravelling = True

    def update(self):
        if self.isTravelling:
            self.distance += self.speed
            self.travelTime += 1

            if self.travelTime == self.totalTravelTime:
                self.isTravelling = False
                self.travelTime = 0

        else:
            self.restTime += 1

            if self.restTime == self.totalRestTime:
                self.isTravelling = True
                self.restTime = 0

        return self

    def updatePoints(self):
        self.points += 1
        return self

def getLeadingReindeer(reindeers):
    distances = []
    for name ,reindeer in reindeers.iteritems():
        distances.append(reindeer.distance)

    return reindeers.keys()[distances.index(max(distances))]

def updateReindeers(reindeers):
    for reindeer in reindeers.itervalues():
        reindeer.update()

    reindeers[getLeadingReindeer(reindeers)].updatePoints()

#read and tokenise input
with open('input') as f:
    input = f.readlines()
    input = map(str.split, map(str.strip, input))

#turn input into dictionairy of obejcts
for instruction in input:
    reindeerName = instruction[0]
    speed = int(instruction[3])
    travelTime = int(instruction[6])
    restTime = int(instruction[13])

    reindeers[reindeerName] = reindeer(speed, travelTime, restTime)

#run simulation
for second in xrange(END_TIME):
    updateReindeers(reindeers)

for reindeer in reindeers.values():
    print reindeer.points
