import utils
import re

IDLE = 0
WORKING = 1

class Worker:
    def __init__(self, ID, constant):
        self.id = ID
        self.constant = constant
        self.state = IDLE
        self.currentJob = None

        self.completionTime = None
        self.currentWorkTime = 1

    def work(self, S, edges, completed):
        if self.state == WORKING:

            if self.currentWorkTime == self.completionTime:
                self.completionTime = None
                self.currentWorkTime = 1
                self.state = IDLE
                completed.add(self.currentJob)

                for m in getChildren(self.currentJob, edges):
                    del edges[edges.index((self.currentJob, m))]
                    if noDependencies(m, edges):
                        S.append(m)
                self.currentJob = None

            self.currentWorkTime += 1

        if self.state == IDLE and S != []:
            S = sorted(S, reverse=True)
            n = S.pop()

            self.currentJob = n
            self.completionTime = ord(self.currentJob) - 64 + self.constant
            self.state = WORKING
            self.currentWorkTime = 1

        return S, edges, completed

def extractFirstLetter(text):
    return re.search(r'(?<=Step )\D', text).group()

def extractSecondLetter(text):
    return re.search(r'(?<=step )\D', text).group()

def getChildren(n, edges):
    return list(map(lambda x: x[1], filter(lambda e: e[0] == n, edges)))

def noDependencies(m, edges):
    return list(filter(lambda e: m == e[1], edges)) == []

def part1(S, edges):
    L = []

    while S != []:
        S = sorted(S, reverse=True)
        n = S.pop()
        L.append(n)

        for m in getChildren(n, edges):
            del edges[edges.index((n, m))]
            if noDependencies(m, edges):
                S.append(m)

    return ''.join(L)

def part2(S, edges, numWorkers, constant, stepCharacters):
    numSeconds = 0
    completed = set()
    workers = [Worker(i, constant) for i in range(numWorkers)]

    print ('Seconds\t W1\t W2')
    while completed != stepCharacters:
        printString = '{0}\t'.format(numSeconds)
        for w in workers:
            S, edges, completed = w.work(S, edges, completed)
            printString += '{0}\t'.format(w.currentJob)

        numSeconds += 1
        print(printString)

    return numSeconds-1

steps = utils.getDay(7)
# steps = ['Step C must be finished before step A can begin.',
#          'Step C must be finished before step F can begin.',
#          'Step A must be finished before step B can begin.',
#          'Step A must be finished before step D can begin.',
#          'Step B must be finished before step E can begin.',
#          'Step D must be finished before step E can begin.',
#          'Step F must be finished before step E can begin.']

stepCharacters = set(map(extractFirstLetter, steps)) | set(map(extractSecondLetter, steps))

edges = []
for s in steps:
    first = extractFirstLetter(s)
    second = extractSecondLetter(s)
    edges.append((first,second))

# Kahn's algorithm

# Find the root nodes
S = []
for c in stepCharacters:
    if noDependencies(c, edges):
        S.append(c)

print (part1(S, edges))

edges = []
for s in steps:
    first = extractFirstLetter(s)
    second = extractSecondLetter(s)
    edges.append((first,second))

# print (part2(S, edges, 2, 0, stepCharacters))
print (part2(S, edges, 5, 60, stepCharacters))
