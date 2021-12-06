import utils

data = utils.get_day(2021, 6)

test_data = ['3,4,3,1,2']

class School:
    def __init__(self, data):
        self._fish = []
        for s in data[0].split(','):
            self._fish.append(int(s))

    def run_1_day(self):
        new_fish = []
        for i in range(len(self._fish)):
            current_fish = self._fish[i]
            if current_fish == 0:
                new_fish.append(8)
                current_fish = 6
            else:
                current_fish -= 1

            self._fish[i] = current_fish

        self._fish += new_fish

    def run_n_days(self, n):
        for _ in range(n):
            self.run_1_day()

    def get_number_of_fish(self):
        return len(self._fish)

test_school = School(test_data)
test_school.run_n_days(18)
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

