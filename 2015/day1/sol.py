current_floor = 0
position_ptr = 1
basement_entered = False

input_file = open('input')
input = input_file.read()
input_file.close()

for character in input:
    if character == '(': current_floor += 1
    elif character == ')': current_floor -= 1
    
    if (current_floor == -1) and (not basement_entered):
        basement_entered = True
        print 'Basement is entered at position ' + str(position_ptr)

    position_ptr += 1

print current_floor
