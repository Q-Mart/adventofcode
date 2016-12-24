import re
import collections

def decrypt(code):
    decryptedCode = ''
    name = re.compile('^\D+(?=\d)').search(code).group().strip("-")
    sectorID = int(re.compile('\d+').search(code).group())
    shiftKey = sectorID % 26

    for char in name:
        if char == '-':
            decryptedCode += ' '
            continue

        newCharCode = ord(char) + shiftKey
        if newCharCode > ord('z'):
            newCharCode -= 26

        decryptedCode += chr(newCharCode)

    return decryptedCode, sectorID

def generateChecksum(name):
    checksum = ''
    name = ''.join(sorted(name))
    mostCommon = collections.Counter(name).most_common()
    chars = [pair[0] for pair in mostCommon]
    counts = [pair[1] for pair in mostCommon]
    equallyFrequentCharacters = ''
    
    for char, count in mostCommon:
        counts.remove(count)
        equallyFrequentCharacters += char
        
        if count not in counts:
            if equallyFrequentCharacters:
                checksum += ''.join(sorted(equallyFrequentCharacters))
                equallyFrequentCharacters = ''

    checksum = checksum[0:5]
    return checksum

def processRoomCodes(listOfCodes, sumOfSectorIDs = 0, listOfRealCodes = []):
    if not listOfCodes:
        return sumOfSectorIDs, listOfRealCodes

    roomCode = listOfCodes.pop()
    checksum = re.compile('\[\D+\]').search(roomCode).group().strip("[]")
    name = re.compile('^\D+(?=\d)').search(roomCode).group().strip("-").replace('-','')

    if generateChecksum(name) == checksum:
        sectorID = int(re.compile('\d+').search(roomCode).group())
        listOfRealCodes.append(roomCode)
        sumOfSectorIDs += sectorID

    return processRoomCodes(listOfCodes, sumOfSectorIDs, listOfRealCodes)

with open('inputs/day4.txt') as f:
    data = f.readlines()

listOfCodes = [line.strip() for line in data]

answer_1, realCodes = processRoomCodes(listOfCodes)
print answer_1

for code in realCodes:
    print decrypt(code)
