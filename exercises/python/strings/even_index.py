def even_index():
    string = str(input('type a string: \n'))
    even_string = ''
    for i in range(0, len(string)):
        if i % 2 == 0:
            even_string = '{}{}'.format(even_string, string[i])
    print(even_string)
