import md5

def hash(string):
    x = md5.new()
    x.update(string)
    return x.digest().encode('hex')

def isValidHash(string):
    return string[:5] == '00000'

def getLetter(string):
    return string[6]

def getPosition(string):
    return int('0x' + string[5], 16)

def getPassword(doorID):
    index = 0
    password = '________'

    while '_' in password:
        h = hash(doorID + str(index))
        index += 1
        if isValidHash(h):
            pos = getPosition(h)

            if (pos >= 8) or (password[pos] != '_'):
                continue
            else:
                password = password[:pos] + getLetter(h) + password[pos+1:]

    return password

with open('inputs/day5.txt') as f:
    data = f.read().strip()

print getPassword(data)
