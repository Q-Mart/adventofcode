import utils

# Part 1
frequencies = list(map(int,utils.getDay(1)))
print (sum(frequencies))

# Part 2
visitedTwice = False
currentFrequency = 0
visitedFrequencies = {currentFrequency: 1}

i = 0
while not visitedTwice:
    f = frequencies[i % len(frequencies)]
    i += 1

    currentFrequency += f
    if currentFrequency in visitedFrequencies:
        visitedFrequencies[currentFrequency] += 1
    else:
        visitedFrequencies[currentFrequency] = 1

    if visitedFrequencies[currentFrequency] == 2:
        visitedTwice = True

print (currentFrequency)
