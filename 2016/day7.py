import re

def hasABBA(string):
    return re.search(r'(.)(?!\1)(.)\2\1', string) != None

def hasTLS(ip):
    for bracketText in re.finditer(r'\[.*?\]', ip):
        if hasABBA(bracketText.group(0)):
            return False
    return hasABBA(ip)

def hypernet_has_bab(ip, bab):
    for md in re.finditer(r'\[.*?\]', ip):
        if md.group(0).find(bab) != -1:
            return True
    return False

def hasSSL(ip):
    for outside in re.split(r'\[.*?\]', ip):
        for match in re.finditer(r'(?=((.)(?!\2).\2))', outside):
            aba = match.group(1)

            if hypernet_has_bab(ip, aba[1] + aba[0] + aba[1]):
                return True

    return False


with open('inputs/day7.txt') as f:
    data = map(str.strip, f.readlines())

print sum(map(hasTLS, data))
print sum(map(hasSSL, data))
