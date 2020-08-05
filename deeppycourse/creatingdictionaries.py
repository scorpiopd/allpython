"""basic structure of dictionary

key : value
immutable=unchanging
int,float,complex,binary,decimal fraction ,strings frozenset--> hashable
tuples-->immutable collection
set ,dictionary,list--> mutable
function()--> immutable

REQUIREMENTS:
the hash of the object must be an integer value
if two objects compare equal the two hashes must be same

more hashes--> slower dictionaries

"""

d={i: i ** 2 for i in range (1,5)}
print(d)
print(hash((1,2,3)))
d={(1,2,3):"this is tuple" }

t1=(1,2,3)
t2=(1,2,3)

print(hash(t1)==hash(t2))
#list are not hashable

def myfunc(a,b):
    return a*b
print(hash(myfunc(1,2)))

d=dict(x=100,a=200)

d={"a":100}
print(d)
print(id(d))
