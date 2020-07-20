def catAndMouse(x, y, z):
    m1 = abs((x - z))
    m2 = abs((y - z))
    if m1 < m2:
        return "Cat A"
    elif m2 < m1:
        return "Cat B"
    else:
        return "Mouse C"


print(catAndMouse(2, 5, 4))
