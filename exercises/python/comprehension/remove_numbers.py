def remove_numbers(numbers):
    return [number for number in numbers if number % 5 != 0 or number % 7 != 0]