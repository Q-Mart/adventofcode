import itertools

LITRES_OF_EGGNOG = 150
#2d list of combinations
combinations = []

with open('input') as f:
    input = map(int, map(str.strip, f.readlines()))

for i in xrange(len(input)):
    for combination in itertools.combinations(input,i):
        combinations.append(combination)

#filter so that we only have combinations which can the fill the eggnog
combinations = filter(lambda x: sum(x) == LITRES_OF_EGGNOG, combinations)
smallest_combinations = min(map(len, combinations))
print len(filter(lambda x: len(x) == 4, combinations))
