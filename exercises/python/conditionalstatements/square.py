import math


def square(number):
    return math.pow(number, 2) if (isinstance(number, float) or isinstance(number, int)) and number < 200 else 200
