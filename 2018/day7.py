import utils
import re

class Node:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parents = set()

def extractFirstLetter(text):
    return re.search(r'(?<=Step )\D', text).group()

def extractSecondLetter(text):
    return re.search(r'(?<=step )\D', text).group()

def getNextStep(availableSteps, nodes, executionSequence):
    temp = []

    foundNextStep = False
    while not foundNextStep:
        s = availableSteps.pop()

        parentsNotYetExecuted = list(filter(lambda x: x not in executionSequence, nodes[s].parents))

        if parentsNotYetExecuted == []:
            foundNextStep = True
            availableSteps += temp
        else:
            temp.append(s)

    availableSteps += temp
    return s, availableSteps

steps = utils.getDay(7)
# steps = ['Step C must be finished before step A can begin.',
#          'Step C must be finished before step F can begin.',
#          'Step A must be finished before step B can begin.',
#          'Step A must be finished before step D can begin.',
#          'Step B must be finished before step E can begin.',
#          'Step D must be finished before step E can begin.',
#          'Step F must be finished before step E can begin.']

stepCharacters = set(map(extractFirstLetter, steps)) | set(map(extractSecondLetter, steps))

nodes = {}
for c in stepCharacters:
    nodes[c] = Node(c)

for s in steps:
    first = extractFirstLetter(s)
    second = extractSecondLetter(s)
    nodes[first].children.add(second)
    nodes[second].parents.add(first)

# Find the root node
root = None
for n in nodes.values():
    if n.parents == set():
        root = n.name
        break

executionSequence = []
usedSteps = [root]
availableSteps = [root]
while availableSteps != []:
    s, availableSteps = getNextStep(availableSteps, nodes, executionSequence)
    executionSequence.append(s)
    print (s)
    for child in nodes[s].children:
        if child not in usedSteps:
            availableSteps.append(child)
            usedSteps.append(child)

    availableSteps = sorted(availableSteps, reverse=True)

print (executionSequence)
