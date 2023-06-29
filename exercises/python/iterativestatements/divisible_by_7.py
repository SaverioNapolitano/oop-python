def divisible_by_7():
    gen = (i for i in range(200) if i % 7 == 0)
    for item in gen:
        print(item)
