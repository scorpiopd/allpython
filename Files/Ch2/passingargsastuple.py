def sumall(*args):
    total = 0
    for num in args:
        total += num
    print(total)


nums = [1, 2, 3, 4, 5]
sumall(*nums)
