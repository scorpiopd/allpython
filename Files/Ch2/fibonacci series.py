
num = int(input("enter number of digits you want in series (minimum 2): "))

first = 0
second = 1

print("\nfibonacci series is:")

for i in range(0, num):
    next = first + second
    print(next, end=", ")

    first = second
    second = next