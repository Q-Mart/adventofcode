import itertools

#(person1, person2): happiness gained by person 1
happinessOf = dict()
listOfTotalHappiness = []
people = set()

def calcHappiness(arrangement):
    happiness = 0
    for i in xrange(len(arrangement)):
        happiness += happinessOf[(arrangement[i], arrangement[(i+1)%len(arrangement)])]


    for i in xrange(len(arrangement) - 1, 0, -1):
        happiness += happinessOf[(arrangement[i]), arrangement[i-1]]

    #get link of last person
    firstPerson = arrangement[0]
    lastPerson = arrangement[len(arrangement) - 1]
    happiness += happinessOf[firstPerson, lastPerson]

    return happiness



with open('input') as f:
    input = f.readlines()
    input = map(str.strip, input)
    input = map(str.split, input)

#turn input into dictionairy
for line in input:
    person1 = line[0]
    person2 = line[len(line) - 1].strip('.')
    happiness = int(line[3])

    people.add(person1)
    people.add(person2)

    if 'gain' in line: happinessOf[(person1, person2)] = happiness
    else: happinessOf[(person1, person2)] = -happiness

#for part 2, add me to the arrangment
for person in people:
    happinessOf[('me', person)] = 0
    happinessOf[(person, 'me')] = 0

people.add('me')

#loop through every permutation
for arrangement in itertools.permutations(list(people)):
    listOfTotalHappiness.append(calcHappiness(arrangement))

print max(listOfTotalHappiness)
