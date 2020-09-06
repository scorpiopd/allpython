#dict

a={11:99,2:137}
a[23]=45 #adding key and value in the dictionary
print(a)

print(len(a))
print(a[2])#printing associated value to the key


 #set coluld not be changed and is always ordered and does not contain any duplicates
s={9,2,3,41}
s.add(66)
print(s)

s={11:99,2:137}
s[23] = 32

for d in s.items():
    print(d)
print(s[11])