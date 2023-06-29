def is_even(number):
    if isinstance(number, int):
        print("It is an even number") if number % 2 == 0 else print("It is an odd number")
