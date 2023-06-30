def remove_duplicates(items): #TODO enhance
    items_no_dup = []
    for item in items:
        if item not in items_no_dup:
            items_no_dup.append(item)
    return items_no_dup

