import re
from itertools import combinations, chain
from copy import deepcopy

microMatcher = re.compile(r'(\w+)-compatible (microchip)')
generatorMatcher = re.compile(r'(\w+) (generator)')

def extract(data):
  return microMatcher.findall(data) + generatorMatcher.findall(data)

def possibleItems(floor):
  #Possible combinations of items that can be taken from the floor
  return chain(combinations(floor, 2), combinations(floor,1))

def children(state):
  currentFloor = state[0]
  newDistance = state[1]+1
  itemsOnFloors = state[2]
  result = []

  for itemsToMove in possibleItems(itemsOnFloors[currentFloor]):
    for item in itemsToMove:
      for i in [-1, 1]:
        newFloor = currentFloor+i
        if 0 <= newFloor < 3:
          newItemsOnFloors = deepcopy(itemsOnFloors)
          newItemsOnFloors[currentFloor].remove(item)
          newItemsOnFloors[newFloor].append(item)
          result.append((newFloor, newDistance, newItemsOnFloors))
    
  return result

def atGoal(state):
  return state[2][:3] == [[],[],[]]

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
      pass
    if atGoal(node):
      return node
    else:
      visitedNodes.append((node[0], node[2]))
      nodesToTry += children(node)

  return "fail"

with open('inputs/day11.txt') as f:
  floors = map(extract, map(str.strip, f.readlines()))

#(current floor number, number of floors moved, array of items on each floor)
currentState = (0, 0, floors)
print bfs(currentState)
