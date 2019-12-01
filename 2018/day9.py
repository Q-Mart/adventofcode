import utils
import collections
import re

class MarbleGame:
    def __init__(self, highestMarble):
        self.circle = collections.deque([0])
        self.nextNumber = 1
        self.currentMarbleIndex = 0
        self.highest = highestMarble
        self.scores = collections.defaultdict(int)

    def insert(self, playerNumber):
        if self.nextNumber % 23 == 0:
            self.scores[playerNumber] += self.nextNumber
            self.nextNumber += 1

            self.circle.rotate(-7)
            self.scores[playerNumber] += self.circle[0]
            del self.circle[0]
            self.circle.rotate(1)

        else:
            self.circle.rotate(1)
            self.circle.insert(0, self.nextNumber)
            self.nextNumber += 1

        return self.circle

    def canPlay(self):
        return self.nextNumber <= self.highest


def playGame(numPlayers, highestMarble):

    game = MarbleGame(highestMarble)

    while game.canPlay():
        for p in range(1, numPlayers+1):
            if game.canPlay():
                game.insert(p)
            else:
                break

    return max(game.scores.values())

assert playGame(9, 25) == 32
assert playGame(10, 1618) == 8317
assert playGame(13, 7999) == 146373
assert playGame(17, 1104) == 2764
assert playGame(21, 6111) == 54718
assert playGame(30, 5804) == 37305

rules = utils.getDay(9)[0]
numPlayers = int(re.search(r'\d+(?= players)', rules).group())
highestMarble = int(re.search(r'\d+(?= points)', rules).group())

print (playGame(numPlayers, highestMarble))
# Part 2
print (playGame(numPlayers, highestMarble*100))
