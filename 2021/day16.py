import utils

def to_binary(num: int) -> str:
    return bin(num)

def to_decimal(string: str) -> int:
    return int(string, 2)

class Packet:
    def __init__(self, hex):
        self._raw = to_binary(int(hex, 16))[2:]
        self._version = to_decimal(self._raw[:3])
        self._type = to_decimal(self._raw[3:6])

    @property
    def version(self):
        return self._version

    @property
    def type(self):
        return self._type

class Value(Packet):
    def __init__(self, hex):
        super().__init__(hex)

        i = 6
        value_str = ''
        while i < len(self._raw) - 5:
            extension = bool(int(self._raw[i]))
            value_str += self._raw[i+1:i+5]

            i += 5
            if extension == False:
                break

        self._value = to_decimal(value_str)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self.value)

data = utils.get_day(2021, 16)[0]

test_1 = Value('D2FE28')
assert test_1.value == 2021
