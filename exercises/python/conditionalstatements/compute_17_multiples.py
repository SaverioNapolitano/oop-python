def compute_17_multiples():
    for item in (number for number in range(300) if number % 17 == 0):
        print(item)
