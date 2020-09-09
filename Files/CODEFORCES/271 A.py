def beautifulyear(y):
    while True:
        y = y+1
        if len(set(str(y))) == len(str(y)):
            break

    return y
