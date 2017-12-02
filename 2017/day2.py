import itertools

def getInput():
    with open('inputs/2.txt') as f:
        data = f.readlines()
        data = list(map(lambda x: x.split('\t'), map(str.strip, data)))
        data = [[int(x) for x in l] for l in data]

    return data

def calcChecksum(spreadsheet):
    differences = [max(row) - min(row) for row in spreadsheet]
    return sum(differences)

def calcEvenlyDivisible(spreadsheet):
    acc = 0
    for row in spreadsheet:
        combos = itertools.combinations(row, 2)
        for x,y in combos:
            if x % y == 0:
                acc += x//y
            elif y % x == 0:
                acc += y//x

    return acc

test = [[5,1,9,5],
        [7,5,3],
        [2,4,6,8]]

test2 = [[5,9,2,8],
         [9,4,7,3],
         [3,8,6,5]]

assert calcChecksum(test) == 18
assert calcEvenlyDivisible(test2) == 9

inp = getInput()
print(calcChecksum(inp))
print(calcEvenlyDivisible(inp))
