class Student:
    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores

    def average_score(self):
        if self.scores:
            average = sum(self.scores) / len(self.scores)
            return average
        else:
            return 0

student = Student("Роман Автомонов", 19, "П-20", [5, 4, 5, 5, 5, 4, 5])
print("Имя:", student.name)
print("Возраст:", student.age)
print("Группа:", student.grade)
print("Оценки:", student.scores)
print("Средний балл:", student.average_score())