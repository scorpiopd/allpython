a = int(input())
b = int(input())

calc = dict(add=a+b, diff=a-b)
for key,value in calc.items():
    print(f"key is {key} and ans is {value}")
