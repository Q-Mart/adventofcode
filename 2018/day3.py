import utils
import re

def genListOfNumbers(claim):
    result = []

    # ID
    result.append(int(re.search("(?<=#)\d+", claim).group()))
    # startX
    result.append(int(re.search("\d+(?=,)", claim).group()))
    # startY
    result.append(int(re.search("\d+(?=:)", claim).group()))
    # width
    result.append(int(re.search("\d+(?=x)", claim).group()))
    # height
    result.append(int(re.search("(?<=x)\d+", claim). group()))

    return result

claims = utils.getDay(3)
# claims = ["#1 @ 1,3: 4x4",
#           "#2 @ 3,1: 4x4",
#           "#3 @ 5,5: 2x2"]

claims = list(map(genListOfNumbers, claims))

# Generate a 2D array to count how many claims need a point of fabric
fabric = [[[] for i in range(1000)] for j in range(1000)]

# Dict containing all iDs that overlap this claim
overlaps = {}

for c in claims:
    iD = c[0]
    startX = c[1]
    startY = c[2]
    width = c[3]
    height = c[4]

    overlaps[iD] = set()

    for x in range(startX, startX+width):
        for y in range(startY, startY+height):
            for number in fabric[y][x]:
                overlaps[number].add(iD)
                overlaps[iD].add(number)

            fabric[y][x].append(iD)

overlappingSquares = 0
for row in fabric:
    for squareInch in row:
        if len(squareInch) > 1:
            overlappingSquares += 1

print (overlappingSquares)
print ([i for i in overlaps if len(overlaps[i]) == 0])
