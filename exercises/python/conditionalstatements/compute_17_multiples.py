def compute_17_multiples():
    number = 17
    total = 1
    while number * total < 300:
        total += 1
    return total - 1
