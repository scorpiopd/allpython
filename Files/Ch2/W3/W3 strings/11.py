#11. Write a Python program to remove the characters which have odd index values of a given string.



#mysol 

a="abcdefgh"
b=list(a)

for i,val in enumerate(b) :
    if i / 2 != 0:
        c=b.pop(i)
        # to print even print(c)
print(b)
        


#using while solution 


a="abcdefgh"
b=list(a)

i=0
while i < len(b):
    if i / 2 !=0:
        b.pop(i)
    i+=1
print(b)



https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

