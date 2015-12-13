import string
import re

alphabet = tuple(string.ascii_lowercase)

def increment(string):
    finalLetter = string[len(string) - 1]
    if finalLetter == 'z':  return increment(string[:len(string) - 1]) + 'a'
    else:
        nextLetter = alphabet[alphabet.index(finalLetter) + 1]
        return string[:len(string) - 1] + nextLetter

def hasThreeStraight(string):
    for i in xrange(len(string) - 2):

        currentLetterIndex = alphabet.index(string[i])
        currentThreeLetters = string[i: i + 3]
        try:
            alphabetThreeLetters = alphabet[currentLetterIndex] + alphabet[currentLetterIndex + 1] + alphabet[currentLetterIndex + 2]
        except IndexError:
            continue

        if alphabetThreeLetters == currentThreeLetters:
            return True

    return False

def hasNoBannedLetters(string):
    return not('i' in string) and not('o' in string) and not('l' in string)

def hasTwoRepititions(string):
    result = re.findall('(?P<letter>[a-z])(?P=letter)', string)
    return len(result) >= 2

def isValid(password):
    return hasTwoRepititions(password) and hasNoBannedLetters(password) and hasThreeStraight(password)

password = 'hepxcrrq'
while not(isValid(password)):
    password = increment(password)

print password

password = increment(password)
while not(isValid(password)):
    password = increment(password)

print password
