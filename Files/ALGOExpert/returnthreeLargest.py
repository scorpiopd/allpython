array = [12, 7, 3, -1, 0,18, 231, 541]


def threelargest(array):
    threel = [None, None, None]

    for num in array:
        updatelargest(threel, num)

    return threel


def updatelargest(threel, num):
    if threel[2] is None or num > threel[2]:
        shiftandupdate(threel,num,2)

    elif threel[1] is None or num > threel[1]:
        shiftandupdate(threel,num,1)

    elif threel[0] is None or num > threel[0]:
        shiftandupdate(threel,num,0)


def shiftandupdate(array, num, idx):
    for i in range(idx+1):
        if i==idx:
            array[i]   = num

        else :
            array[i]=array[i+1]
print(threelargest(array))

