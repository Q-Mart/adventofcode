import utils
import re
import networkx

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

def part2(steps):
    G = networkx.DiGraph()
    for s in steps:
        G.add_edge(extractFirstLetter(s), extractSecondLetter(s))

    print (''.join(networkx.lexicographical_topological_sort(G)))

    taskTimes = []
    tasks = []
    time = 0

    while taskTimes or G:
        availableTasks = [t for t in G if t not in tasks and G.in_degree(t) == 0]
        if availableTasks and len(taskTimes) < 5:
            task = min(availableTasks)
            taskTimes.append(ord(task)-4)
            tasks.append(task)
        else:
            minTime = min(taskTimes)
            completed = [tasks[i] for i, v in enumerate(taskTimes) if v == minTime]
            taskTimes = [v - minTime for v in taskTimes if v > minTime]
            tasks = [t for t in tasks if t not in completed]
            time += minTime
            G.remove_nodes_from(completed)

    return time

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
print (part2(steps))
