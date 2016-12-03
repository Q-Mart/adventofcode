no_visited_houses = 0

def mapFrequency(input):
    visited_houses = {}
    x = 0
    y = 0

    #Robo santa
    x1 = 0
    y1 = 0

    for i in xrange(len(input)):

        isOddIteration = i%2
        char = input[i]

        if isOddIteration:

            if char == '^': y += 1
            if char == 'v': y -= 1
            if char == '>': x += 1
            if char == '<': x -= 1

            try:
                visited_houses[(x,y)] += 1
            except KeyError:
                visited_houses[(x,y)] = 0

        else:

            if char == '^': y1 += 1
            if char == 'v': y1 -= 1
            if char == '>': x1 += 1
            if char == '<': x1 -= 1

            try:
                visited_houses[(x1,y1)] += 1
            except KeyError:
                visited_houses[(x1,y1)] = 0

    return visited_houses

with open('input') as i:
    input = i.read()

no_visited_houses += len(mapFrequency(input))
print 'Santa visited ' + str(no_visited_houses) + ' houses this Christmas'
