#12 Write a Python program to count the occurrences of each word in a given sentence. Go to the editor

a="abcdabcd"
b={}

for i in a:
    i=i.strip()
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
for i1 in b.items():
    print(i1)
print(b)



https://www.geeksforgeeks.org/python-count-occurrences-of-each-word-in-given-text-file-using-dictionary/
