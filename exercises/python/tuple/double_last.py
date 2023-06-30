def double_last(items): #TODO enhance
    for ind, item in enumerate(items):
        new_item = []
        for index, element in enumerate(item):
            new_item.append(element if index != len(item) - 1 else element * 2)
        items[ind] = tuple(new_item)
    return items
