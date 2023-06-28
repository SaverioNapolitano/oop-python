def reverse(string):
    new_string = ''
    if isinstance(string, str) and len(string) % 4 == 0:
        for i in range(len(string) - 1, -1, -1):
            new_string = '{}{}'.format(new_string, string[i])
        return new_string
    return string
