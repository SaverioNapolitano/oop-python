def remove_char(string, index):
    if isinstance(string, str) and len(string) > 0 and isinstance(index, int) and index < len(string):
        return '{}{}'.format(string[: index], string[index+1:])
