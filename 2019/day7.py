import utils
import itertools

data = utils.get_day(2019, 7)
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
        self.inputs = [0,0]
        self.inputs_ptr = 0
        self.PHASE_SETTING_INDEX = 0
        self.SIGNAL_INDEX = 1

        self.input_phase_once = False
        self.waiting = False
        self.finished = False
        self.next = None

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
        if self.finished:
            return True

        should_halt = False

        if self.waiting:
            return should_halt

        opcode = [int(x) for x in str(self.data[self.ip])]

        # Add trailing 0s
        while len(opcode) < 5:
            opcode = [0] + opcode

        instruction = int(str(opcode[-2])+str(opcode[-1]))
        param_1_ptr = self.ip+1
        param_2_ptr = self.ip+2

        if instruction == HALT:
            should_halt = True
            self.finished = True

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
            self.store_data(param_1_ptr, self.inputs[self.inputs_ptr], opcode[-3])
            if self.input_phase_once:
                self.inputs_ptr = self.SIGNAL_INDEX
            else:
                self.inputs_ptr = (self.inputs_ptr + 1) % 2
            self.ip += 2

        elif instruction == OUTPUT:
            self.inputs[self.SIGNAL_INDEX] = self.get_data(param_1_ptr, opcode[-3])
            self.ip += 2
            self.waiting = True

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
        self.inputs_ptr = 0

        should_halt = False
        while not should_halt:
            should_halt = self.step()

        return self.data

    def run_with_phase_setting(self, phase_setting, data):
        self.run(data)

    def run_with_wait(self):
        should_halt =  False
        while (not should_halt) or (not self.waiting):
            should_halt = self.step

        return should_halt

def test_with_feedback_loop(data, order):
    computers = list()
    for i in range(5):
        computers.append(Intcode())
        computers[i].data = data.copy()
        computers[i].input_phase_once = True
        computers[i].inputs[computers[i].PHASE_SETTING_INDEX] = phase_setting

    for i in range(5):
        computers[i].next = computers[(i+1)%5]

    signal_input = 0

    all_finished = False
    while not all_finished:
        for i in range(len(order)):
            computers[i].inputs[computers[i].SIGNAL_INDEX] = signal_input
            computers[i].run_with_phase_setting(order[i], computers[i].data)
            signal_input = computers[i].inputs[computers[i].SIGNAL_INDEX]

        all_finished = True
        for c in computers:
            all_finished = all_finished & c.finished

    return signal_input

test_1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
assert(test(test_1, [4,3,2,1,0]) == 43210)

test_2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
assert(test(test_2, [0,1,2,3,4]) == 54321)

test_3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
          1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
assert(test(test_3, [1,0,4,3,2]) == 65210)

max_signal_output = 0
for x in itertools.permutations(range(5)):
    o = test(data, x)
    if o > max_signal_output:
        max_signal_output = o

utils.print_part_1(max_signal_output)

test_4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
print(test_with_feedback_loop(test_4, [9,8,7,6,5]))
