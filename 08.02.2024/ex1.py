import math

class Circle:
    def __init__(self, dia, h):
        self._dia = dia
        self._h = h
        self._area = self.make_area(dia)

    # Метод для расчёта площади
    def make_area(self, dia):
        r = dia / 2
        area = math.pi * r**2
        return area

    # Свойства для доступа к диаметру
    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, value):
        self._dia = value
        self._area = self.make_area(value)

    # Свойства для доступа к высоте
    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value

    # Защищённое свойство для доступа к площади
    @property
    def area(self):
        return self._area

a = Circle(5, 10)
print("Диаметр:", a.dia)
print("Высота:", a.h)
print("Площадь:", a.area)

a.dia = 8
print("Диаметр:", a.dia)
print("Высота:", a.h)
print("Площадь:", a.area)

a.h = 15
print("Диаметр:", a.dia)
print("Высота:", a.h)
print("Площадь:", a.area)

a.area = 50