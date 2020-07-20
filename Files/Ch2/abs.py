num= int(input())
val = abs(1000-num) and abs(2000-num)
if val <=100 :
    print("True")
else :
    print("false")

""""""""""""""""
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
"""""""""