def split(string, delimiter):
    if isinstance(string, str):
        return string.rsplit(delimiter, 1)
