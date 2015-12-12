total_difference = 0

def getDiff(string):
    return len(string) - len(eval(string))

def encode(string):
    encoded_string = ''

    for char in string:
        if char == '"': encoded_string += '\\\"'
        elif char == '\\': encoded_string += '\\\\'
        else: encoded_string += char

    return '"' + encoded_string + '"'

with open('input') as f:
    input = f.readlines()
    input = map(str.strip, input)

for line in input:
    total_difference += getDiff(line)

print total_difference

total_difference = 0

for line in input:
    total_difference += getDiff(encode(line))

print total_difference
