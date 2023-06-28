import math


def sum_squared():
    squared_sum = 0
    number = 1
    while number <= 100:
        squared_sum += math.pow(number, 2)
        number += 1
    return squared_sum
