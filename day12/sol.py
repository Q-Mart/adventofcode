import json
import re

def total(input):
    return sum(map(int, re.findall('-?[0-9]+', input)))

def containsRed(object):
    return 'red' in object

def removeRed(input):
    if 'red' in input.values(): return {}
    else: return input

with open('input') as f:
    input = f.read()
    json_input = json.loads(input, object_hook=removeRed)

print total(input)
print total(str(json_input))
