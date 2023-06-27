def reverse(string):
    new_string = ''
    if isinstance(string, str) and string.__len__() % 4 == 0:
        for i in range(string.__len__() - 1, -1, -1):
            new_string = '{}{}'.format(new_string, string[i])
        return new_string
    return string
