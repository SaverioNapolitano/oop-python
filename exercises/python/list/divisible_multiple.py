def divisible_multiple():
    print(', '.join((str(number) for number in range(200, 301) if number % 7 == 0 and number % 5 != 0)))
