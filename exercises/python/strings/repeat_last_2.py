def repeat_last_2(string):
    if isinstance(string, str) and len(string) >= 2:
        return 4 * '{}'.format(string[-2:])
