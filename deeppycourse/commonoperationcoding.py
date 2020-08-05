d= dict(zip("abc",range(1,3)))
print(d)



print(d.get("a"))
print(d.get("python","NA"))



"""+++++++++++++++++++++++++++++++++++
a= int(input())
for i in range (a):



    d= dict(zip(range(1,a) ,range(1,a)))
print(d)
++++++++++++++++++++++++++++++++++++++++"""






"""+++++++++++++++++++++++++++++++++++

text="Traditionally, a text is understood to be a piece of written or spoken material in its primary form (as opposed to a paraphrase or summary). A text is any stretch of language that can be understood in context. It may be as simple as 1-2 words" \
     " (such as a stop sign) or as complex as a novel. Any sequence of sentences that belong together can be considered a text."

counts =dict()
for i in text :
    counts[i] =counts.get(i,0) + 1
print(counts)

++++++++++++++++++++++++++++++++++++++++"""








"""+++++++++++++++++++++++++++++++++

# modification to not consider white spaces and lower and upper letters counts will be the same
counts=dict()

for m in text:
    key=m.lower().strip()
    if key:
     counts[key] =counts.get(key,0) + 1

print(counts)
++++++++++++++++++++++++++++++++++"""





"""+++++++++++++++++++++++++++++++++
# deleting keys from the dictionaries

d= dict.fromkeys("abcd",2)
print(d)

del d ["a"]
print(d)
++++++++++++++++++++++++++++++++++"""




"""+++++++++++++++++++++++++++++++++
d=dict({i: i **2 for i in range (1,5)})
print(d)
d.popitem()
print(d)
++++++++++++++++++++++++++++++++++"""