sues = dict()

class sue():
    def __init__(self):
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None

#result of the MFCSAM
match = sue()
match.children = 3
match.cats = 7
match.samoyeds = 2
match.pomeranians = 3
match.akitas = 0
match.vizslas = 0
match.goldfish = 5
match.trees = 3
match.cars = 2
match.perfumes = 1

with open('input') as f:
    input = f.readlines()
    input = map(str.split, map(str.strip, input))

#parse input into object dictionary
for instruction in input:
    number = int(instruction[1].strip(':'))
    sues[number] = sue()

    for i in xrange(len(instruction)):
        word = instruction[i]
        if word == 'children:':
            sues[number].children = int(instruction[i+1].strip(','))
        elif word == 'cats:':
            sues[number].cats = int(instruction[i+1].strip(','))
        elif word == 'samoyeds:':
            sues[number].samoyeds = int(instruction[i+1].strip(','))
        elif word == 'pomeranians:':
            sues[number].pomeranians = int(instruction[i+1].strip(','))
        elif word == 'akitas:':
            sues[number].akitas = int(instruction[i+1].strip(','))
        elif word == 'vizslas:':
            sues[number].vizslas = int(instruction[i+1].strip(','))
        elif word == 'goldfish:':
            sues[number].goldfish = int(instruction[i+1].strip(','))
        elif word == 'trees:':
            sues[number].trees = int(instruction[i+1].strip(','))
        elif word == 'cars:':
            sues[number].cars = int(instruction[i+1].strip(','))
        elif word == 'perfumes:':
            sues[number].perfumes = int(instruction[i+1].strip(','))

mostLikelyAunty = 0
highestMatches = 0

for key, aunty in sues.iteritems():
    matches = 0

    #match against our sample
    if aunty.children == match.children: matches += 1
    if aunty.cats == match.cats: matches += 1
    if aunty.samoyeds == match.samoyeds: matches += 1
    if aunty.pomeranians == match.pomeranians: matches += 1
    if aunty.akitas == match.akitas: matches += 1
    if aunty.vizslas == match.vizslas: matches += 1
    if aunty.goldfish == match.goldfish: matches += 1
    if aunty.trees == match.trees: matches += 1
    if aunty.cars == match.cars: matches += 1
    if aunty.perfumes == match.perfumes: matches += 1


    if matches > highestMatches:
        highestMatches = matches
        mostLikelyAunty = key

print mostLikelyAunty
