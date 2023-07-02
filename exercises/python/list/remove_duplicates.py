def remove_duplicates(items):
    items_no_dup = []
    for item in items:
        if item not in items_no_dup:
            items_no_dup.append(item)
    return items_no_dup

