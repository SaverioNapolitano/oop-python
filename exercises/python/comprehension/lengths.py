def lengths():
    sentence = "the quick brown fox jumps over the lazy dog"
    print(sentence.split())
    print([len(word) for word in sentence.split() if word != 'the'])
