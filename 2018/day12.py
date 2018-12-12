import utils
import re

MARGIN = ''.join(['.' for i in range(10000)])

def getInitialState(data):
    return re.search(r'(?<=initial state: )[#\.]+', data).group()

def getNote(data):
    first = re.search(r'[#\.]+(?= =>)', data).group()
    second = re.search(r'(?<==> )[#\.]', data).group()
    return (first, second)

def nextGeneration(currentState, notes):
    nextState = list(currentState)
    for i in range(len(currentState)-4):
        if currentState[i:i+5] in notes.keys():
            replacement = notes[currentState[i:i+5]]
            nextState[i+2] = replacement

    return ''.join(nextState)

def sumState(state):
    acc = 0
    currentIndex = -len(MARGIN)
    for c in state:
        if c == '#':
            acc += currentIndex
        currentIndex += 1

    return acc

def sumAfterGenerations(initialState, notes, numGenerations):
    state = initialState
    for i in range(numGenerations):
        state = nextGeneration(state, notes)
    return sumState(state)


rawData = utils.getDay(12)

initialState = MARGIN + getInitialState(rawData[0]) + MARGIN
notes = dict()
for i in range(2, len(rawData)):
    first, second = getNote(rawData[i])
    notes[first] = second

print (sumAfterGenerations(initialState, notes, 20))

# Part 2
sumAfter116 = sumAfterGenerations(initialState, notes, 116)
total = sumAfter116 + ((50000000000 - 116) * 55)
print (total)
