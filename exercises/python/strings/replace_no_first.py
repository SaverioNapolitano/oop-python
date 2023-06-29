def replace_no_first(string):
    if isinstance(string, str):
        return '{}{}'.format(string[0], string[1:].replace(string[0], '$'))
