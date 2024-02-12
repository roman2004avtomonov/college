class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hours_worked = 0
        self.salary_per_hour = self._get_salary_per_hour()
        self.total_salary = 0

    def _get_salary_per_hour(self):
        if self.position == "Junior":
            return 10
        elif self.position == "Middle":
            return 15
        elif self.position == "Senior":
            return 20

    def work(self, time):
        self.hours_worked += time
        self.total_salary += self.salary_per_hour * time

    def rise(self):
        if self.position == "Senior":
            self.salary_per_hour += 1

    def info(self):
        return f"{self.name} {self.hours_worked}ч. {self.total_salary}тгр."


programmer = Programmer("Roman", "Middle")

programmer.work(8)

programmer.rise()

info = programmer.info()

print(info)