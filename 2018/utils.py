import re

def getDay(dayNumber):
    lines = []
    with open("inputs/{0}.txt".format(dayNumber)) as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))
    return lines

def getNumbers(string):
    return re.findall(r'-?\d+').group()
