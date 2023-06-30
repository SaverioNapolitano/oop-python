def count_alpha(string):
    if isinstance(string, str):
        return {key: string.count(key) for key in string}
