import utils
from collections import defaultdict

data = utils.get_day(2021, 6)

test_data = ['3,4,3,1,2']

class School:
    def __init__(self, data):
        self._fish = defaultdict(int)
        for s in data[0].split(','):
            self._fish[int(s)] += 1

    def run_1_day(self):
        new_fish = defaultdict(int)
        for timer, number_of_fish in self._fish.items():
            if timer == 0:
                new_fish[8] += number_of_fish
                new_fish[6] += number_of_fish
            else:
                new_fish[timer-1] += number_of_fish

        self._fish = new_fish

    def run_n_days(self, n):
        for i in range(n):
            self.run_1_day()

    def get_number_of_fish(self):
        return sum(self._fish.values())

test_school = School(test_data)
test_school.run_n_days(18)
print(test_school.get_number_of_fish())
assert(test_school.get_number_of_fish() == 26)

test_school = School(test_data)
test_school.run_n_days(80)
assert(test_school.get_number_of_fish() == 5934)

school = School(data)
school.run_n_days(80)
utils.print_part_1(school.get_number_of_fish())

test_school = School(test_data)
test_school.run_n_days(256)
assert(test_school.get_number_of_fish() == 26984457539)

school = School(data)
school.run_n_days(256)
utils.print_part_2(school.get_number_of_fish())
