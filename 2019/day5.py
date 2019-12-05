import utils

data = utils.get_day(2019, 5)
data = [list(map(int, elem.split(','))) for elem in data][0]

POSITION_MODE = 0
IMMEDIATE_MODE = 1

ADD = 1
MULT = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99

class Intcode():
    def __init__(self):
        self.data = None
        self.ip = 0

    def store_data(self, ptr, value, parameter_mode):
        if parameter_mode == IMMEDIATE_MODE:
            self.data[ptr] = value
        elif parameter_mode == POSITION_MODE:
            self.data[self.data[ptr]] = value
        else:
            print('\033[93mError! Landed on unknown parameter mode {0}\033[0m'.format(parameter))

    def get_data(self, ptr, parameter_mode):
        if parameter_mode == IMMEDIATE_MODE:
            return self.data[ptr]
        elif parameter_mode == POSITION_MODE:
            return self.data[self.data[ptr]]
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

        else:
            should_halt = True
            print('\033[93mError! Landed on unknown opcode {0}\033[0m'.format(instruction))


        return should_halt

    def run(self, data):
        self.data = data
        self.ip = 0

        should_halt = False
        while not should_halt:
            should_halt = self.step()

        return self.data

computer = Intcode()

data_copy = data.copy()
computer.run(data_copy)
