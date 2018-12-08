import utils
import re

def extractFirstLetter(text):
    return re.search(r'(?<=Step )\D', text).group()

def extractSecondLetter(text):
    return re.search(r'(?<=step )\D', text).group()

def getChildren(n, edges):
    return list(map(lambda x: x[1], filter(lambda e: e[0] == n, edges)))

def noDependencies(m, edges):
    return list(filter(lambda e: m == e[1], edges)) == []

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

L = []

while S != []:
    S = sorted(S, reverse=True)
    n = S.pop()
    L.append(n)

    for m in getChildren(n, edges):
        del edges[edges.index((n, m))]
        if noDependencies(m, edges):
            S.append(m)

print (''.join(L))
