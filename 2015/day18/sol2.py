#Part 2 solution
ON = '#'
OFF = '.'
STEPS = 100

board = []

with open('input') as f:
    board = map(str.strip, f.readlines())

def evolve(board):
    newBoard = []
    length = len(board)

    for y in xrange(length):
        newYString = ''
        for x in xrange(length):
            state = board[y][x]
            #handle the corners
            if x in (0,length-1) and y in (0,length-1):
                newYString += ON
                continue
            #now handle the sides
            elif y == 0: numberNeighboursOn = len(filter(lambda x: x == ON,[board[y][x-1],board[y][x+1],board[y+1][x],board[y+1][x+1],board[y+1][x-1]]))
            elif y == length-1: numberNeighboursOn = len(filter(lambda x: x == ON,[board[y][x-1],board[y][x+1],board[y-1][x],board[y-1][x+1],board[y-1][x-1]]))
            elif x == 0: numberNeighboursOn = len(filter(lambda x: x == ON,[board[y+1][x],board[y][x+1],board[y-1][x],board[y-1][x+1],board[y+1][x+1]]))
            elif x == length-1: numberNeighboursOn = len(filter(lambda x: x == ON,[board[y-1][x],board[y][x-1],board[y+1][x-1],board[y-1][x-1],board[y+1][x]]))
            else:
                neighbours = [board[y-1][x-1],board[y-1][x],board[y-1][x+1],
                              board[y][x-1], board[y][x+1],
                              board[y+1][x-1],board[y+1][x],board[y+1][x+1]]
                numberNeighboursOn = len(filter(lambda x: x == ON, neighbours))

            if state == ON and numberNeighboursOn in (2,3): newYString += ON
            elif state == OFF and numberNeighboursOn == 3: newYString += ON
            else: newYString += OFF

        newBoard.append(newYString)
    return newBoard

#switch on corners
board[0] = ON + board[0][1:len(board)-1] + ON
board[len(board) - 1] = ON + board[len(board) - 1][1:len(board)-1] + ON
for step in xrange(STEPS):
    board = evolve(board)

print sum(map(len, [filter(lambda x: x==ON, line) for line in board]))
