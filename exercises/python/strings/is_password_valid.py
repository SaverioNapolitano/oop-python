def is_password_valid(string):
    return isinstance(string, str) and 6 <= string.__len__() <= 12 and (string.isnumeric() or string.isdigit())
