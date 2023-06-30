import operator


def sorting_tuples_multilevel(people):
    return sorted(people, key=operator.itemgetter(0, 1, 2))
