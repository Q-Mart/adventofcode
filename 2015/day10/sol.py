input = '1113222113'

def lookAndSay(input):
    output = ''
    current_number = ''
    current_frequency = ''

    for char in input:
        if char != current_number:
            output += str(current_frequency) + str(current_number)
            current_number = char
            current_frequency = 1
        else:
            current_frequency += 1

    output += str(current_frequency) + str(current_number)
    return output

for i in xrange(50):
    input = lookAndSay(input)

print len(input)
