def first_2_last_2(string):
    new_string = ''
    if isinstance(string, str) and len(string) >= 2:
        new_string = '{}{}'.format(string[0:2], string[-2:])
    return new_string
