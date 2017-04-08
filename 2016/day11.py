import re
from itertools import combinations, chain
from copy import deepcopy

microMatcher = re.compile(r'(\w+)-compatible (microchip)')
generatorMatcher = re.compile(r'(\w+) (generator)')

def extract(data):
  return microMatcher.findall(data) + generatorMatcher.findall(data)

def extractPairs(floors):
  """
  returns a list of 2 integer tuples for each element in the form of
  (floor number for the generator, floor number for the microchip)
  """

  pairs = {}
  for floorNum in xrange(len(floors)):
    for device in floors[floorNum]:
      element = device[0]
      deviceType = device[1]
      if element in pairs:
        if deviceType == 'generator':
          pairs[element] = [floorNum] + pairs[element]
        else:
          pairs[element] += [floorNum]
      else:
        pairs[element] = [floorNum]

  return map(tuple, pairs.values())

def children(state):
  results = []
  currentFloor = state[0]
  items = list(state[2])
  pairsOnFloor = []

  for pair in items:
    if currentFloor in pair:
      pairsOnFloor.append(pair)

  possiblePairsToTake = chain(combinations(pairsOnFloor,1), combinations(pairsOnFloor,2))

  for pairs in possiblePairsToTake:
    print "pairs: " + str(pairs)
    for i in [-1, 1]:
      newFloor = currentFloor + i
      if newFloor>3 or newFloor<0:
        continue

      newItems = list(items)
      for pair in pairs:
        indexOfItem = pair.index(currentFloor)
        newItems.remove(pair)
        newItems = newItems + [pair[:indexOfItem] + (newFloor,) + pair[indexOfItem+1:]]
      results.append((newFloor, state[1]+1, newItems, state))
  return results

def isValid(state):
  currentFloor = state[0]
  items = list(state[2])
  pairsOnFloor = []

  pairsOnFloor = filter(lambda pair: currentFloor in pair, items)
  pairsOnFloor = filter(lambda pair: pair.count(currentFloor) != 2, pairsOnFloor)
  if len(pairsOnFloor) <= 1:
    return True
  microChipsPresentOnFloor = bool(len(filter(lambda pair: pair.index(currentFloor) == 1, pairsOnFloor)))
  generatorsPresentOnFloor = bool(len(filter(lambda pair: pair.index(currentFloor) == 0, pairsOnFloor)))
  if not(microChipsPresentOnFloor) and not(generatorMatcher):
    return True

  return microChipsPresentOnFloor != generatorsPresentOnFloor

def atGoal(state):
  pairs = state[2]
  return filter(lambda x: x != (3,3), pairs) == []

def bfs(root):
  nodesToTry = []
  visitedNodes = []
  if atGoal(root):
    return root

  visitedNodes.append((root[0], root[2]))
  nodesToTry = children(root)
  while nodesToTry:
    node = nodesToTry.pop(0)
    if (node[0], node[2]) in visitedNodes:
      continue

    if not(isValid(node)):
      continue

    print node[2]
    if atGoal(node):
      return node
    else:
      visitedNodes.append((node[0], node[2]))
      nodesToTry += children(node)

  return "fail"

with open('inputs/day11.txt') as f:
  floors = map(extract, map(str.strip, f.readlines()))

#(current floor number, number of floors moved, current list of pairs)
pairs = extractPairs(floors)
currentState = (0, 0, pairs, "Parent")
print bfs(currentState)
