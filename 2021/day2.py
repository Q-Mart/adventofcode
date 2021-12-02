import utils

class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    def forward(self, x):
        self.horizontal += x

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x

    def read_instructions(self, instructions):
        for cmd, amount in instructions:
            if cmd == 'forward':
                self.forward(amount)
            elif cmd == 'up':
                self.up(amount)
            elif cmd == 'down':
                self.down(amount)
            else:
                raise Exception(f"Unknown cmd {cmd}")

class Sub2(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, x):
        super().forward(x)
        self.depth += self.aim * x

    def up(self, x):
        self.aim -= x

    def down(self, x):
        self.aim += x

instructions = list(
    map(
        lambda x: (x.split()[0], int(x.split()[1])),
        utils.get_day(2021, 2)
    )
)

test_instructions = [
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2)
]

sub = Submarine()
sub.read_instructions(test_instructions)
assert(sub.horizontal * sub.depth == 150)

sub = Submarine()
sub.read_instructions(instructions)
utils.print_part_1(sub.horizontal * sub.depth)

sub = Sub2()
sub.read_instructions(test_instructions)
assert(sub.horizontal * sub.depth == 900)

sub = Sub2()
sub.read_instructions(instructions)
utils.print_part_2(sub.horizontal * sub.depth)
