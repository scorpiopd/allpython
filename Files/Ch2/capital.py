s = input()
a=s.split()
for f in a :
    w=(f[0].title() + f[1:])



print(w,end=" ")



#also you can use .capitalize instead of .title

#approach2
"""""""""
s=input("enter")
print(s[0].capitalize()+s[1:7])
"""""