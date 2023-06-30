import random


def random_from_list():
    print(random.choice([number for number in range(0, 201) if number % 5 == 0 and number % 7 == 0]))