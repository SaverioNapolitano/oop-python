def parser(string):
    if isinstance(string, str) and string.__len__() >= 3:
        if string[-3:] == 'ing':
            string = '{}{}'.format(string, 'ly')
        else:
            string = '{}{}'.format(string, 'ing')
    return string