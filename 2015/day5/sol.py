import re

niceCounter = 0

def hasThreeVowels(input):
    result = re.search('[aeiou].*[aeiou].*[aeiou]', input)
    return hasattr(result, 'group')

def hasTwoInARow(input):
    result = re.search('^.*(?P<letter>[a-z])(?P=letter).*', input)
    return hasattr(result, 'group')

def noBannedStrings(input):
    result = re.search('ab|cd|pq|xy',input)
    return not hasattr(result, 'group')

def noOverlappingPairs(input):
    result = re.search(r'(..).*\1', input)
    return hasattr(result, 'group')

def repeatingLetter(input):
    result = re.search('(?P<letter>[a-z])[a-z](?P=letter)', input)
    return hasattr(result, 'group')

def isNice(input):
    return hasThreeVowels(input) and hasTwoInARow(input) and noBannedStrings(input)

def isNice2(input):
    return noOverlappingPairs(input) and repeatingLetter(input)

with open('input') as f:
    input = f.readlines()

for string in input:
    if isNice2(string): niceCounter += 1

print niceCounter
