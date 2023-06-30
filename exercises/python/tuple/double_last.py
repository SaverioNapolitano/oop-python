def double_last(items):
    return [tuple([(element if index != len(item) - 1 else element * 2) for index, element in enumerate(item)])
            for item in items]
