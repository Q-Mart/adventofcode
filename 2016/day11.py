import re
import math
from itertools import combinations, chain
from copy import deepcopy
from heapq import heappush, heappop

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

  listOfItemsOnFloors = list(sum(items, ()))
  itemsAvailable = []
  for i in xrange(len(listOfItemsOnFloors)):
    if listOfItemsOnFloors[i] == currentFloor:
      itemsAvailable.append(i)

  indexesToTake = chain(combinations(itemsAvailable,1), combinations(itemsAvailable,2))

  for indexes in indexesToTake:
    for i in [-1, 1]:
      newFloor = currentFloor + i
      if newFloor>3 or newFloor<0:
        continue

      listOfItemsOnFloors = list(sum(items,() ))
      for index in indexes:
        listOfItemsOnFloors[index] = newFloor

      it = iter(listOfItemsOnFloors)
      newItems = zip(it, it)

      newState = (newFloor, state[1]+1, newItems)
      if isValid(newState):
        results.append(newState)
  return results

def isValid(state):
  currentFloor = state[0]
  items = list(state[2])
  pairsOnFloor = []

  #get the pairs on the current floor
  pairsOnFloor = filter(lambda pair: currentFloor in pair, items)
  #we only care about the microchips/generators that are not with their 'partner'
  pairsOnFloor = filter(lambda pair: pair.count(currentFloor) != 2, pairsOnFloor)
  microChipsPresentOnFloor = bool(len(filter(lambda pair: pair.index(currentFloor) == 1, pairsOnFloor)))
  generatorsPresentOnFloor = bool(len(filter(lambda pair: pair.index(currentFloor) == 0, pairsOnFloor)))
  return not(microChipsPresentOnFloor) or not(generatorsPresentOnFloor)

def atGoal(state):
  pairs = state[2]
  return filter(lambda x: x != (3,3), pairs) == []

def h(state):
  #flatten pairs into list
  listOfItemsOnFloors = list(sum(list(state[2]), ()))
  total = sum(len(floor) * i for (i, floor) in enumerate(reversed(list(state[2]))))
  # return reduce(lambda acc, item: acc + (3-item), listOfItemsOnFloors, 0)
  return math.ceil(total / 2)


def aStar(root):
  frontier = [(0, root)]
  visitedNodes = []
  (f,currentNode) = heappop(frontier)
  while not atGoal(currentNode):
    while (currentNode[0], currentNode[2]) in visitedNodes:
      (f,currentNode) = heappop(frontier)

    visitedNodes.append((currentNode[0], currentNode[2]))
    for child in children(currentNode):
      g = child[1]
      f = g + h(child)
      heappush(frontier, (f, child))
    

  return currentNode

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
print aStar(currentState)
