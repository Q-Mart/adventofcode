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
    def __init__(self, version, subpackets):
        super().__init__(version)
        self._subpackets = subpackets

    def __repr__(self):
        string = f'Operator(version={self._version}, subpackets=['
        for packet in self._subpackets:
            string += str(packet) + ','

        string = string[:-2]
        string += '])'
        return string

def parse_val(raw):
    version = int(raw[:3])
    raw = raw[6:]

    i = 0
    value_str = ''
    while i < len(raw) - 5:
        extension = bool(int(raw[i]))
        value_str += raw[i+1:i+5]

        i += 5
        if extension == False:
            break

    return Value(version=version, val=to_decimal(value_str)), raw[i:]

def parse_operator(raw):
    version = int(raw[:3])
    raw = raw[6:]

    length_type = int(raw[0])
    raw = raw[1:]

    print(f'length_type: {length_type}')
    if length_type == 0:
        length = to_decimal(raw[:15])
        raw = raw[15:]

        subpackets = []
        to_parse = raw[:length]

        r = parse(to_parse)
        while r != None:
            new_sub, remainder = r
            subpackets.append(new_sub)
            r = parse(remainder)

    else:
        print('NOT IMPLEMENTED')
        return

    print(f'length: {length}')

    return Operator(version, subpackets), raw

def parse(raw):
    if len(raw) < 11:
        return None

    type = to_decimal(raw[3:6])

    if type == 4:
        return parse_val(raw)
    else:
        return parse_operator(raw)

data = utils.get_day(2021, 16)[0]

test_1, _ = parse(to_binary('D2FE28'))
assert test_1.value == 2021

test_2, _ = parse(to_binary('38006F45291200'))
print(test_2)
