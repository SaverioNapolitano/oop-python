def is_password_valid(string):
    return isinstance(string, str) and 6 <= len(string) <= 12 and (string.isnumeric() or string.isdigit())
