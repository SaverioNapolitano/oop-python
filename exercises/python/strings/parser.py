def parser(string):
    if isinstance(string, str) and len(string) >= 3:
        if string[-3:] == 'ing':
            string = '{}{}'.format(string, 'ly')
        else:
            string = '{}{}'.format(string, 'ing')
    return string