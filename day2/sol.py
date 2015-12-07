needed_paper = 0
input = []

def area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def slack(l, w, h):
    return min(l*w, w*h, h*l)

with open('input') as i:
    current_line = i.readline()

    while current_line != '':
        #parse through input and split into lists containing numbers
        input.append(current_line[:len(current_line) - 1].split('x'))
        current_line = i.readline()

for present in input:
    l = int(present[0])
    w = int(present[1])
    h = int(present[2])

    needed_paper += area(l,w,h) + slack(l,w,h)

print 'We need ' + str(needed_paper) + ' square feet of wrapping paper'
