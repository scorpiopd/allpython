name = "Pranav"
single = list(map(str, name))

print(single[0])
for n in name:
    print(n[0], end=" ")

for number in range(1, 7):
    print(number * number)

a = len(name)
for b in range(a):
    print(name)


for r in  range(1,10,2):
    print("******")

count=0
while count < 10:
    print("i will rule python")
    count+=1


r =range(10)
print(list(r))

a=input(" how many times  i have to tell you to clean up your room")
b=int(a)
count=0
while count < b :
#for i in range(b):


    print(f"ok i have told you {a} times get up bastard1 ")
    count+=1


a =range(1,20)

for b in a:
    if   b== 4 or b==13:
        print(f"{b} is unlucky")

    elif b%2==1:
        print(f"{b}  is even")

    else:
        print(f"{b} is odd")


msg=input("whats password")
while msg !="a":
    print("wrong")
    break
else:
    print("right")