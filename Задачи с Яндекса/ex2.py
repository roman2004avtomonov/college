import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, other_point):
        distance = math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)
        return round(distance, 2)


point = Point(3, 4)

point.move(-2, 3)

print(point.x, point.y)

other_point = Point(6, 8)

distance = point.length(other_point)

print(distance)
