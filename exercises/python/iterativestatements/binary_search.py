def binary_search(sorted_list, item): #TODO see teacher solution
    if isinstance(sorted_list, list):
        start = 0
        end = len(sorted_list) - 1
        while start <= end:
            index = int((start + end) / 2)
            if sorted_list[index] == item:
                return index
            if sorted_list[index] > item:
                end = index - 1
            else:
                start = index + 1
        return -1


