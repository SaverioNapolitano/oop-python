def remove_index(items, index):
    return items[:index] + items[index + 1:]
    # return tuple(item for ind, item in enumerate(items) if ind != index)
