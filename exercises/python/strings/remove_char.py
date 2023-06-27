def remove_char(string, index):
    if isinstance(string, str) and string.__len__() > 0 and isinstance(index, int) and index < string.__len__():
        return '{}{}'.format(string[0: index], string[index+1:])
