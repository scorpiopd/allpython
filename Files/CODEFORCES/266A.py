n=int(input())
stones=input()

counter=0

for i in range(1,n):
    if stones[i] == stones[i-1]:
        counter+=1
print(counter)