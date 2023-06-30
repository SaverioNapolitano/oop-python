def list_product(first_list, second_list):
    if len(first_list) == len(second_list):
        return [first * second for first, second in zip(first_list, second_list)]
