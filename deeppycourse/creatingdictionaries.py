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
