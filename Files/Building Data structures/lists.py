alist = [56, 72, 4, 8, 5]
print(alist)
n = int(input("enter a number to append "))
alist.append(n)
print(alist)
print(alist[0])
alist[0]=99
print(alist)
print(len(alist))
print((map(sorted(alist), alist)))



