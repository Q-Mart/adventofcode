current_floor = 0

input_file = open('input')
input = input_file.read()
input_file.close()

for character in input:
    if character == '(': current_floor += 1
    elif character == ')': current_floor -= 1

print current_floor
