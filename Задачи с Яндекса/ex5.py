import math


class Rectangle:
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2

    def perimeter(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        perimeter = 2 * (width + height)
        return round(perimeter, 2)

    def area(self):
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        area = width * height
        return round(area, 2)


rect = Rectangle((-2, 3), (4, -5))

perimeter = rect.perimeter()
area = rect.area()

print(perimeter)
print(area)