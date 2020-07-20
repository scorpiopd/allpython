from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests
"""
names="praga","lala","haman","paman","ladf"

for name in names:
    print(name.title())

first_half_alphabet=list(string.ascii_lowercase)[:13]
print(first_half_alphabet)

newnames=[]
for name in names:
    if name[0] in first_half_alphabet:
        newnames.append(name)
print(newnames)

newnames2= [name.title()for name in names if name[0] in first_half_alphabet]
print(newnames2)"""

resp=requests.get("https://www.w3.org/TR/PNG/iso_8859-1.txt")
words=resp.text.lower().split()
words[:5]
print(words)

cnt=Counter(words)
common=cnt.most_common(5)
print(common)
