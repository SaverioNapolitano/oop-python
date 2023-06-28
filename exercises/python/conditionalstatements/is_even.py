def is_even(number):
    if isinstance(number, int):
        if number % 2 == 0:
            print("It is an even number")
        else:
            print("It is an odd number")