import utils
from collections import namedtuple

Zone = namedtuple('Zone', ['x1', 'x2', 'y1', 'y2'])

class Probe:
    def __init__(self, vx, vy, target: Zone):
        self._vx = vx
        self._vy = vy
        self._x = 0
        self._y = 0

        self._target = target

        self._max_y = 0
        self._hit_target = False

    def step(self):
        if self._in_target():
            self._hit_target = True

        if self._y > self._max_y:
            self._max_y = self._y

        self._x += self._vx
        self._y += self._vy

        if self._vx > 0:
            self._vx -= 1
        elif self._vx < 0:
            self._vx += 1
        else:
            self._vx = 0

        self._vy -= 1

    def _in_target(self):
        within_x = self._target.x1 <= self._x <= self._target.x2
        within_y = self._target.y1 <= self._y <= self._target.y2
        return within_x and within_y

    def past_target(self):
        past_x = self._x > self._target.x2
        past_y = self._y < self._target.y2
        return past_x or past_y

    @property
    def max_y(self):
        return self._max_y

    @property
    def hit_target(self):
        return self._hit_target

def parse_input(data):
    _ , xy = data.split(':')
    x, y = xy.split(',')

    x = x.strip()
    x = x[2:]
    x1, x2 = x.split('..')

    y = y.strip()
    y = y[2:]
    y1, y2 = y.split('..')

    return Zone(int(x1), int(x2), int(y1), int(y2))

def max_y_for_zone(z: Zone):
    max_y = 0

    y_step = range(z.y2*1000)
    if z.y2 < 0:
        y_step = range(0, -(z.y2*1000))

    x_step = range(z.x2)
    if z.x2 < 0:
        x_step = range(0, z.x2, -1)

    for vy in y_step:
        for vx in x_step:
            p = Probe(vx, vy, z)

            while not p.past_target():
                p.step()

            if p.hit_target:
                if p.max_y > max_y:
                    max_y = p.max_y

    return max_y

data = utils.get_day(2021, 17)

test = 'target area: x=20..30, y=-10..-5'
test_zone = parse_input(test)
print(max_y_for_zone(test_zone))
