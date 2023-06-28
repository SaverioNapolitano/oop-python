def pitagoric_table():
    line = ''
    for i in range(1, 11):
        line = '{}{}|'.format(line, str(i).center(10))
    line = '|{}|{}'.format('x'.center(10), line)
    separator = '-'*len(line)
    print(separator)
    print(line)
    print(separator)
    for row in range(1, 10):
        line = '|{}|'.format(str(row).center(10))
        for col in range(1, 11):
            res = row*col
            line = '{}{}|'.format(line, str(res).center(10))
        print(line)
        print(separator)
