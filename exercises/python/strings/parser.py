def parser(string):
    if isinstance(string, str) and len(string) >= 3:
        return '{}{}'.format(string, 'ly') if string[-3:] == 'ing' else '{}{}'.format(string, 'ing')

