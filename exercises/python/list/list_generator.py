def list_generator(sequence):
    if isinstance(sequence, str):
        return sequence.split(',')
