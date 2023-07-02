import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('radius has to be a positive number')
        self._radius = value

    def perimeter(self):
        return 2 * math.pi * self._radius

    def area(self):
        return self._radius ** 2 * math.pi
