strin="google.com"

d={}

for i in strin:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)


#https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/



#to remove duplicates
a=[5,2,5,1,3,4,4]

d={}

for i in a:
    if i in d:
        d[i]=True
        
    else:
        d[i]=False
print(d.keys())
