#dictionary that maps wire:signal
wires = {}
MAX_SIGNAL = 65535

def parse(instruction):
    result = instruction[1]
    expression = instruction[0]
    #check for numeric assignment
    try:
        wires[result] = int(expression)
    except ValueError:
        #otherwise, it is an algebraic expression
        #tokenise the expression
        expression = expression.split()
        wires[result] = expression

def evaluate(wire):
    try:
        return int(wire)

    except ValueError:
        pass

    if type(wires[wire]) == int:
        result = wires[wire]

    elif wires[wire][0] == 'NOT':
        target = wires[wire][1]
        result = MAX_SIGNAL - evaluate(target)

    elif len(wires[wire]) == 1:
        target = wires[wire][0]
        result = evaluate(target)

    else:
        left = wires[wire][0]
        operator = wires[wire][1]
        right = wires[wire][2]

        if operator == 'AND': result = evaluate(left) & evaluate(right)
        elif operator == 'OR': result = evaluate(left) | evaluate(right)
        elif operator == 'LSHIFT': result = evaluate(left) << int(right)
        elif operator == 'RSHIFT': result = evaluate(left) >> int(right)

    wires[wire] = result
    return result

with open('input') as f:
    input = f.readlines()

#make input more computer readable
for i in xrange(len(input)):
    input[i] = input[i].split('->')
    input[i] = map(str.strip, input[i])

for instruction in input:
    parse(instruction)

print evaluate('a')
