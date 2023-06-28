def fibonacci(integer):  # TODO see teacher recursive variant
    a = 0
    b = 1
    return_list = [a, b]
    if integer == 0:
        return 0
    if integer == 1:
        return 1
    while True:
        c = a + b
        a = b
        b = c
        if c > integer:
            break
        return_list.append(c)
    return return_list
