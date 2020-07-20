
#to count words


words = """hello myself pranav studying in kbp college college of engineering satara"""
w = words.split()

commonwords = {}
for word in w:
    if word not in commonwords :
        commonwords[word] = 0
    commonwords[word] += 1


for k, v in sorted(commonwords.items()):
    print(k, v)

# we can use counter from collection module
from collections import Counter
v=Counter(w)
print(v)
