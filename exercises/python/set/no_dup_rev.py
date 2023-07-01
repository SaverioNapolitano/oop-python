def no_dup_rev(items):
    if isinstance(items, list):
        items.reverse()
    reversed_items = []
    for item in items:
        if item not in reversed_items:
            reversed_items.append(item)
    return reversed_items
