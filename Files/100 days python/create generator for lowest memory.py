"""def gen():
    for i in range(5):
        yield i

gen()
print(next(gen()))"""

"""for i in gen():
    print(next(gen()))
"""

"""2)
options=["red","blue","green","blue"]
def creategen(options=options):
    for option in options:
     yield f"option value ={option}"

print(list(creategen()))
"""

names=["arnold sdhawanger"," bob belderos"," alec baldwin ","alex carry"," hoalm jadahav"]


for n in  names:
   print( n.title())

def reverse_first(n):

    first,last=n.split()
    return f"{last} and{first}"
a=[reverse_first(n) for n in names]
print(a)

