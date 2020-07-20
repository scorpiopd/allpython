numlist = [1, 2, 3, 4, 5]
numlist.reverse()
print(numlist)

numlist = [1, 2, 3, 4, 5]

fl = []
for num in numlist:
    fl.insert(0, num)
print(fl)

z = numlist[::-1]
print(z)

for num in numlist:
    print(str(num))

mystring = "shruti"
print(list(mystring))
l = list(mystring)
print(l[0:3])
print(l.pop())
print(l)
l.insert(6, 'i')
print(l)
l.insert(7, 'h')
print(l)
del l[6]
print(l)
l.append('s')#append will always add to the end
