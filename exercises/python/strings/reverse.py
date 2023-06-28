def reverse(string):
    if isinstance(string, str) and len(string) % 4 == 0:
       string = string[::-1]
    return string
