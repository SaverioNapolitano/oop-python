import math


def square(number):
    if (isinstance(number, float) or isinstance(number, int)) and number < 200:
        return math.pow(number, 2)
    else:
        return 200
