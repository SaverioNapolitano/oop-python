def remove_index(items, index):
    return tuple(item for ind, item in enumerate(items) if ind != index)