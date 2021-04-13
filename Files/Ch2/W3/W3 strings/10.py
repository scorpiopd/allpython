a="hello"

b=len(a)-1
v=a[1:b]

print(a[-1]+v+a[0])

#rather than creating an extra variable v
#print(a[-1]+a[1:b]+a[0])

#oneliner
#print(a[-1]+a[1:-1]+a[0])



