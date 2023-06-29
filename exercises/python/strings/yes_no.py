def yes_no(string):
    print('Yes') if isinstance(string, str) and string.lower() == 'yes' else print('No')
