from random import sample


def random_list():
    print(sample([number for number in range(100, 201)], 5))
