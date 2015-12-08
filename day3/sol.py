no_visited_houses = 1

def mapFrequency(input):
    visited_houses = {}
    x = 0
    y = 0

    for char in input:
        if char == '^': y += 1
        if char == 'v': y -= 1
        if char == '>': x += 1
        if char == '<': x -= 1

        try:
            visited_houses[(x,y)] += 1
        except KeyError:
            visited_houses[(x,y)] = 0

    return visited_houses

with open('input') as i:
    input = i.read()

no_visited_houses += len(mapFrequency(input))
print 'Santa visited ' + str(no_visited_houses) + ' houses this Christmas'
