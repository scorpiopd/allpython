array = [5, 1, 22, 25, 6, -1, 8, 10]

subsequnce = [1, 6, -1, 10]


def validatesubsequence(array, subsequnce):
    arrayidx = 0
    subidx = 0
    while arrayidx < len(array) and subidx < len(subsequnce):
        if array[arrayidx] == subsequnce[subidx]:
            subidx += 1
        else:
            arrayidx += 1
    return subidx == len(subsequnce)


print(validatesubsequence(array, subsequnce))
