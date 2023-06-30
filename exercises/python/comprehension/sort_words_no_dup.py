def sort_words_no_dup(string):
    if isinstance(string, str):
        return ' '.join(item for item in sorted(list(set(string.split()))))
