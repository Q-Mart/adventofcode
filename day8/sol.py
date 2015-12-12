total_difference = 0

def getDiff(string):
    return len(string) - len(eval(string))

with open('input') as f:
    input = f.readlines()
    input = map(str.strip, input)

for line in input:
    total_difference += getDiff(line)

print total_difference
