class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._lenght

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError('length has to be a positive number')
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('width has to be a positive number')
        self._width = value

    def perimeter(self):
        return 2 * (self._width + self._length)

    def area(self):
        return self._width * self._length
