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
        return f'Value(version={self._version}, val={self._value})'

class Operator(Packet):
    def __init__(self, version, subpackets):
        super().__init__(version)
        self._subpackets = subpackets

    def __repr__(self):
        string = f'Operator(version={self._version}, subpackets=['
        for packet in self._subpackets:
            string += str(packet) + ','

        string = string[:-1]
        string += '])'
        return string

def parse_val(raw):
    version = to_decimal(raw[:3])
    raw = raw[6:]

    extension = True
    value_str = ''
    while extension == True:
        extension = bool(int(raw[0]))
        raw = raw[1:]
        value_str += raw[:4]
        raw = raw[4:]

    return Value(version=version, val=to_decimal(value_str)), raw

def parse_operator(raw):
    version = to_decimal(raw[:3])
    raw = raw[6:]

    length_type = int(raw[0])
    raw = raw[1:]

    subpackets = []
    print(f'length_type: {length_type}')
    if length_type == 0:
        length = to_decimal(raw[:15])
        raw = raw[15:]

        to_parse = raw[:length]

        r = parse(to_parse)
        while r != None:
            new_sub, remainder = r
            subpackets.append(new_sub)
            print(new_sub, remainder)
            r = parse(remainder)

        raw = raw[length:]

    else:
        num_subpackets = to_decimal(raw[:11])
        raw = raw[11:]

        for _ in range(num_subpackets):
            new_sub, raw = parse(raw)
            subpackets.append(new_sub)

    return Operator(version, subpackets), raw

def parse(raw):
    if len(raw) < 11:
        return None

    type = to_decimal(raw[3:6])

    if type == 4:
        return parse_val(raw)
    else:
        return parse_operator(raw)

def sum_version_numbers(token, current_sum=0):
    if type(token) == Value:
        return current_sum + token.val

data = utils.get_day(2021, 16)[0]

test_1, _ = parse(to_binary('D2FE28'))
assert test_1.value == 2021

test_2, _ = parse(to_binary('38006F45291200'))
expected_2 = Operator(version=1, subpackets=[Value(version=6, val=10), Value(version=2, val=20)])

test_3, _ = parse(to_binary('EE00D40C823060'))
expected_3 = Operator(version=7, subpackets=[Value(version=2, val=1), Value(version=4, val=2), Value(version=1, val=3)])
