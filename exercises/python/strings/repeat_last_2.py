def repeat_last_2(string):
    if isinstance(string, str) and string.__len__() >= 2:
        return 4 * '{}'.format(string[-2:])
