import itertools

LITRES_OF_EGGNOG = 150
#2d list of combinations
combinations = []

with open('input') as f:
    input = map(int, map(str.strip, f.readlines()))

for i in xrange(len(input)):
    for combination in itertools.combinations(input,i):
        combinations.append(combination)

print len(filter(lambda x: sum(x) == LITRES_OF_EGGNOG, combinations))
