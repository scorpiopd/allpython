# 9. Write a Python program to get a new string from a given string where
# "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

#first type
a=input("enter")
a.split()

if a[0:2] == "is":
    print(a)
else:
    fullsec="is " + a

    print(fullsec)

#second type

a=input("enter ")
if "is"  in a:
    print(a)
else:
    print("is "+a)






#third type

a=["is a"]
b=[]
for g in a:
    if "is" in g[0:]:
        print(g)

else:
    if "is "not in g:

     b.append("is"+g)
     print(b)