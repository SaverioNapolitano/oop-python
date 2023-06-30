import itertools


def sentences():
    print(tuple([(subject, verb, obj) for subject, verb, obj in itertools.combinations(["I", "You", "Play", "Love",
                                                                                        "Hockey", "Football"], 3) if
                 subject in ["I", "You"] and verb in ["Play", "Love"] and obj in ["Hockey", "Football"]]))
