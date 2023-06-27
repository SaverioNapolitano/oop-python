def concatenate_invert(first_string, second_string):
    if isinstance(first_string, str) and isinstance(second_string, str):
        return '{}{} {}{}'.format(second_string[0:-1], first_string[-1], first_string[0:-1], second_string[-1])
