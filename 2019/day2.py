import utils

data = utils.get_day(2019, 2)
data = [list(map(int, elem.split(','))) for elem in data][0]

ADD = 1
MULT = 2
HALT = 99

class Intcode():
    def __init__(self):
        self.data = None
        self.ptr = 0

    def add(self, param1_ptr, param2_ptr, result_ptr):
        self.data[result_ptr] = self.data[param1_ptr] + self.data[param2_ptr]

    def mult(self, param1_ptr, param2_ptr, result_ptr):
        self.data[result_ptr] = self.data[param1_ptr] * self.data[param2_ptr]

    def step(self):
        should_halt = False

        instruction = self.data[self.ptr]
        param1_ptr = self.data[self.ptr+1]
        param2_ptr = self.data[self.ptr+2]

        if instruction == HALT:
            should_halt = True
        elif instruction == ADD:
            self.add(param1_ptr, param2_ptr, self.data[self.ptr+3])
        elif instruction == MULT:
            self.mult(param1_ptr, param2_ptr, self.data[self.ptr+3])
        else:
            should_halt = True
            print('\033[93mError! Landed on unknown opcode {0}\033[0m'.format(instruction))

        self.ptr += 4

        if self.ptr > len(self.data) - 5:
            # End of data, going further will result in out of bounds error
            should_halt = True

        return should_halt

    def run(self, data):
        self.data = data
        self.ptr = 0

        should_halt = False
        while not should_halt:
            should_halt = self.step()

        return self.data

computer = Intcode()

assert(computer.run([1,0,0,0,99]) == [2,0,0,0,99])
assert(computer.run([2,3,0,3,99]) == [2,3,0,6,99])
assert(computer.run([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
assert(computer.run([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
assert(computer.run([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50])

data_copy = data.copy()
data_copy[1] = 12
data_copy[2] = 2
utils.print_part_1(computer.run(data_copy)[0])

TARGET = 19690720

for noun in range(100):
    for verb in range(100):
        data_copy = data.copy()
        data_copy[1] = noun
        data_copy[2] = verb

        if computer.run(data_copy)[0] == TARGET:
            utils.print_part_2(100 * noun + verb)
            break
