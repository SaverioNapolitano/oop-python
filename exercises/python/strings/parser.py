def parser(string):
    if isinstance(string, str) and len(string) >= 3:
        if string[-3:] == 'ing':
            return '{}{}'.format(string, 'ly')
        else:
            return '{}{}'.format(string, 'ing')
