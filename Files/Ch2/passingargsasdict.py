# 1
def displayname(first, second):
    print(f"hello {first} says hello to {second}")


# names=dict(first="colt",second="Pranav")
names = {"first": "Colt", "second": "Pranav"}
displayname(**names)


# 2

def multiply(a, b):
    print(a * b)


data = dict(a=3, b=4)
# data = {"a":2,"b":8}
multiply(**data)
