def sort_words(sequence):
    if isinstance(sequence, str):
        return ','.join(sorted(sequence.split(',')))
