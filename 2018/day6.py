import utils

def dist(c1, c2):
    # Manhattan distance
    # c1 and c2 are tuples (x, y) of coords
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

coords = utils.getDay(6)
coords = list(map(lambda x: x.replace(',', ''), coords))
coords = list(map(str.split, coords))
coords = list(map(lambda x: (int(x[0]), int(x[1])), coords))
# coords = [(1, 1),
#           (1, 6),
#           (8, 3),
#           (3, 4),
#           (5, 5),
#           (8, 9)]


def part1():
    maxX = max(map(lambda x: x[0], coords))
    maxY = max(map(lambda x: x[1], coords))

    board = [[-1 for i in range(maxX+1)] for j in range(maxY+1)]


    # Find the closest points on the visible part of the board
    for y in range(maxY+1):
        for x in range(maxX+1):
            distances = {k: v for k, v in enumerate(map(lambda c: dist(c, (x,y)), coords))}

            # sort by value
            distances = sorted(distances.items(), key=lambda kv: kv[1])

            # check that the two smallest distances are not equal
            if distances[0][1] == distances[1][1]:
                board[y][x] = '.'
            else:
                board[y][x] = distances[0][0]

    # Exclude anthing on the perimeter of the board, as it extends to infinity
    excluded = set(board[0]) | set(board[maxY])
    for y in range(1, maxY):
        excluded |= {board[y][0], board[y][maxX]}
    excluded -= {'.'}

    greatestPopulation = 0
    coordID = None

    for i in range(len(coords)):
        if i in excluded:
            continue

        currentPopulation = 0
        for row in board:
            currentPopulation += len(list(filter(lambda x: x==i, row)))

        if currentPopulation > greatestPopulation:
            greatestPopulation = currentPopulation
            coordID = i

    print (coordID, greatestPopulation)

def part2(boundry):
    maxX = max(map(lambda x: x[0], coords))
    maxY = max(map(lambda x: x[1], coords))

    board = [[-1 for i in range(maxX+1)] for j in range(maxY+1)]


    counter = 0

    for y in range(maxY+1):
        for x in range(maxX+1):
            distances = sum(map(lambda c: dist(c, (x,y)), coords))

            if distances < boundry:
                board[y][x] = distances
                counter += 1

    print (counter)


part1()
part2(10000)
