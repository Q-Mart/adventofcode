import collections

def getInput():
    with open('inputs/4.txt') as f:
        data = f.readlines()
        data = list(map(str.split, map(str.strip, data)))
        data = [[''.join(sorted(x)) for x in l] for l in data]
    return data

validPassphrases = 0
passphrases = getInput()
for pssph in passphrases:
    c = collections.Counter(pssph)
    if max(c.values()) == 1: validPassphrases += 1

print(validPassphrases)
