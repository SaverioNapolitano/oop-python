def longer_words(words): #TODO enhance
    min_length = len(words[0])
    for word in words:
        if len(word) < min_length:
            min_length = len(word)
    return [word for word in words if len(word) > min_length]
