import utils

def to_binary(num: str) -> str:
    num_nibbles = len(num) * 4
    return (bin(int(num,16))[2:]).zfill(num_nibbles)

def to_decimal(string: str) -> int:
    return int(string, 2)

class Packet:
    def __init__(self, version):
        self._version = version

    @property
    def version(self):
        return self._version

class Value(Packet):
    def __init__(self, version, val):
        super().__init__(version)
        self._value = val

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)

class Operator(Packet):
    def __init__(self, version, sub_packets):
        super().__init__(version)
        self._sub_packets = sub_packets

def parse_val(raw):
    i = 0
    value_str = ''
    while i < len(raw) - 5:
        extension = bool(int(raw[i]))
        value_str += raw[i+1:i+5]

        i += 5
        if extension == False:
            break

    return to_decimal(value_str)

def parse_operator(raw):
    ptr = 6
    length_type = int(raw[ptr])
    ptr += 1

    print(f'length_type: {length_type}')
    length = None
    if length_type == 0:
        print(ptr, ptr+15)
        print(raw[ptr:ptr+15])
        length = to_decimal(raw[ptr:ptr+15])
        ptr += 15
    else:
        length = to_decimal(raw[ptr:ptr+11])
        ptr += 11

    print(f'length: {length}')

    sub_packets = parse(raw[ptr:ptr+length])
    return sub_packets

def parse(raw):
    version = to_decimal(raw[:3])
    type = to_decimal(raw[3:6])

    print(version, type)
    if type == 4:
        val = parse_val(raw[6:])
        return Value(version, val)

    else:
        sub_packets, ptr = parse_operator(raw)

        return packets

data = utils.get_day(2021, 16)[0]

test_1 = parse(to_binary('D2FE28'))
assert test_1.value == 2021

test_2 = parse(to_binary('38006F45291200'))
