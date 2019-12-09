import utils

data = utils.get_day(2019, 9)
data = [list(map(int, elem.split(','))) for elem in data][0]

POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2

ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
ADJUST_RELATIVE_BASE_OFFSET = 9
HALT = 99

class Intcode():
    def __init__(self):
        self.data = None
        self.relative_base_offset = 0
        self.ip = 0

    def store_data(self, ptr, value, parameter_mode):
        if parameter_mode == IMMEDIATE_MODE:
            self.data[ptr] = value
        elif parameter_mode == POSITION_MODE:
            self.data[self.data[ptr]] = value
        elif parameter_mode == RELATIVE_MODE:
            self.data[self.data[ptr]+self.relative_base_offset] = value
        else:
            print('\033[93mError! Landed on unknown parameter mode {0}\033[0m'.format(parameter))

    def get_data(self, ptr, parameter_mode):
        if parameter_mode == IMMEDIATE_MODE:
            return self.data[ptr]
        elif parameter_mode == POSITION_MODE:
            return self.data[self.data[ptr]]
        elif parameter_mode == RELATIVE_MODE:
            return self.data[self.data[ptr]+self.relative_base_offset]
        else:
            print('\033[93mError! Landed on unknown parameter mode {0}\033[0m'.format(parameter))

    def step(self):
        should_halt = False

        opcode = [int(x) for x in str(self.data[self.ip])]

        # Add trailing 0s
        while len(opcode) < 5:
            opcode = [0] + opcode

        instruction = int(str(opcode[-2])+str(opcode[-1]))
        param_1_ptr = self.ip+1
        param_2_ptr = self.ip+2

        if instruction == HALT:
            should_halt = True

        elif instruction == ADD:
            result_ptr = self.ip+3
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            param_2 = self.get_data(param_2_ptr, opcode[-4])
            self.store_data(result_ptr, param_1+param_2, opcode[-5])
            self.ip += 4

        elif instruction == MULT:
            result_ptr = self.ip+3
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            param_2 = self.get_data(param_2_ptr, opcode[-4])
            self.store_data(result_ptr, param_1*param_2, opcode[-5])
            self.ip += 4

        elif instruction == INPUT:
            data = int(input('Input data:\n'))
            self.store_data(param_1_ptr, data, opcode[-3])
            self.ip += 2

        elif instruction == OUTPUT:
            print('Output data:\n{0}'.format(self.get_data(param_1_ptr, opcode[-3])))
            self.ip += 2

        elif instruction == JUMP_IF_TRUE:
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            if param_1 != 0:
                self.ip = self.get_data(param_2_ptr, opcode[-4])
            else:
                self.ip += 3

        elif instruction == JUMP_IF_FALSE:
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            if param_1 == 0:
                self.ip = self.get_data(param_2_ptr, opcode[-4])
            else:
                self.ip += 3

        elif instruction == LESS_THAN:
            result_ptr = self.ip+3
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            param_2 = self.get_data(param_2_ptr, opcode[-4])
            if param_1 < param_2:
                val = 1
            else:
                val = 0

            self.store_data(result_ptr, val, opcode[-5])
            self.ip += 4

        elif instruction == EQUALS:
            result_ptr = self.ip+3
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            param_2 = self.get_data(param_2_ptr, opcode[-4])
            if param_1 == param_2:
                val = 1
            else:
                val = 0

            self.store_data(result_ptr, val, opcode[-5])
            self.ip += 4

        elif instruction == ADJUST_RELATIVE_BASE_OFFSET:
            param_1 = self.get_data(param_1_ptr, opcode[-3])
            self.relative_base_offset += param_1
            self.ip += 2

        else:
            should_halt = True
            print('\033[93mError! Landed on unknown opcode {0}\033[0m'.format(instruction))


        return should_halt

    def run(self, data):
        self.data = data
        self.ip = 0
        self.relative_base_offset = 0

        #Add extra space
        for i in range(10*len(self.data)):
            data.append(0)

        should_halt = False
        while not should_halt:
            should_halt = self.step()

        return self.data

computer = Intcode()

print('############ BEGIN TEST ##############')

# tests
test_1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
computer.run(test_1)

test_2 = [1102,34915192,34915192,7,4,7,99,0]
computer.run(test_2)

test_3 = [104,1125899906842624,99]
computer.run(test_3)

print('############ END TEST ##############')

data_copy = data.copy()
computer.run(data_copy)
