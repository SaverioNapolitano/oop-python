def count_odd_even(*args):
    even = 0
    odd = 0
    for number in args:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
