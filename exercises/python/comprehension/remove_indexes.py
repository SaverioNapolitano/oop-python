def remove_indexes(numbers):
    return [number for index, number in enumerate(numbers) if index not in [0, 2, 4, 6]]
