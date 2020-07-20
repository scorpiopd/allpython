def nearf(n):
    return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
print(nearf(int(input())))
