def square_list():
    numbers = []
    for number in range(1, 21):
        numbers.append(number**2)
    return numbers
    #compact version
    #return [number**2 for number in range(1, 21)]