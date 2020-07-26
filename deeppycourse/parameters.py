# parameter defaults

def additem(name,quantity,unit,grocery=[]):
    grocery.append("({0},({1},{2})".format(name,quantity,unit,grocery))

    return grocery

store1=[]
store2=[]

print(additem("banana",2,"units",store1))


print(additem("python",1,"medium-rare",store2))
print(store1 is store2)
if store1 is store2:
    print("same bro")

else:
    print("not same bro")


# calculating factorial
"""def factorial(n):
    if n <1 :
        return 1
    else:
        print(f"calculating {n}")
    return n * factorial(n-1)

print(factorial(3))"""


#factorial using cached values

def fact(n,cache={}):
    if n < 1:
        return 1

    elif n in cache :
        print(f"val from {n}")
        return cache[n]


    else :
        print(f"calculating {n}")
        result = n * fact(n-1)
        cache[n]= result
        return result




print(fact(3))
