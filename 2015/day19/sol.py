import re

stringToReplace = ''
replacements = []
possibleStringReplacements = set()
counter = 0

with open('input') as f:
    replacements = map(str.strip, f.readlines())
    stringToReplace = replacements.pop()
    #get rid of trailing newline
    replacements.pop()
    replacements = map(lambda x: x.split('=>'), replacements)
    replacements = map(lambda x: map(str.strip, x), replacements)


for pattern in replacements:
    molecule = pattern[0]
    replacement = pattern[1]

    regex = re.compile(molecule)

    for r in regex.finditer(stringToReplace):
        index = r.start()
        counter += 1
        print r.group()
        if index == len(stringToReplace)-1:
            possibleStringReplacements.add(stringToReplace[:index] + stringToReplace[index].replace(molecule, replacement))
        else:
            possibleStringReplacements.add(stringToReplace[:index] + stringToReplace[index].replace(molecule, replacement) + stringToReplace[index+1:])

print len(possibleStringReplacements)
print counter
