import sys
import pygame
import time

pygame.init()

ON = '#'
OFF = '.'
STEPS = 100

GAME_EVOLVING = True
WHITE = (255,255,255)
BLACK = (0,0,0)

board = []

stepNumber = 0

screen = pygame.display.set_mode((500,500),0,32)

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
            if x == 0 and y == 0: numberNeighboursOn = len(filter(lambda x: x == ON, [board[0][1], board[1][0], board[1][1]]))
            elif x == length-1 and y == 0: numberNeighboursOn = len(filter(lambda x: x == ON, [board[0][length-2], board[1][length-1], board[1][length-2]]))
            elif x == 0 and y == length-1: numberNeighboursOn = len(filter(lambda x: x == ON, [board[length-1][1], board[length-2][0], board[length-2][1]]))
            elif x == length-1 and y == length-1: numberNeighboursOn = len(filter(lambda x: x == ON, [board[length-1][length-2], board[length-2][length-1], board[length-2][length-2]]))
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(BLACK)

    for y in xrange(len(board)-1):
        for x in xrange(len(board)-1):
            if board[y][x] == ON: pygame.draw.rect(screen, WHITE, (50*x,50*y,50,50))
            else: pygame.draw.rect(screen, BLACK, (5*x,5*y,5,5))

    if stepNumber != STEPS:
        board = evolve(board)
        stepNumber += 1
        time.sleep(0.1)


    pygame.display.update()
