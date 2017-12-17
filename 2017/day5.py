def getInput():
    with open('inputs/5.txt') as f:
        data = f.readlines()
        data = list(map(lambda x: int(x), map(str.strip, data)))
    return data

def process(instructions):
    steps = 0
    ptr = 0
    while ptr < len(instructions):
        tmp = ptr + instructions[ptr]
        instructions[ptr] += 1
        ptr = tmp
        steps += 1

    return steps

def process2(instructions):
    steps = 0
    ptr = 0
    while ptr < len(instructions):
        tmp = ptr + instructions[ptr]
        if instructions[ptr] >= 3:
            instructions[ptr] -= 1
        else:
            instructions[ptr] += 1
        ptr = tmp
        steps += 1

    return steps

test = [0, 3, 0, 1, -3]
assert process(test) == 5
test = [0, 3, 0, 1, -3]
assert process2(test) == 10

print(process(getInput()))
print(process2(getInput()))
