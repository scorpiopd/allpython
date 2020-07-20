a = (2, 4, 6, 9)
for val in a:

    if type(val) != int:
     raise TypeError("must be an integer")
colors=["red","violet","white"]
c=input("enter a color ")

if c not in colors:
    raise ValueError("ahh color you entered not mathching")
else:
    print("matching entered color ")


