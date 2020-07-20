#Problem1
#addition of only odd numbers

def sumodd (numbers):
    total =0
    for n in numbers:
        if n %2 != 0 :
            total +=n
    return total
print(sumodd([1,2,3,4,5]))




""""""""""""""""
#Problem2
#check which num is bigger 
def number(a,b):
    if a>b:
        return "First is big"
    elif b>a:
        return "second is big "
    return "numbers are equal"

print(number(6,8))


#Problem3
# getting list as input and then converting to integer and printing square of number


nums = input()

num = list(map(int, nums))
def square():
    u = [x * x for x in num]
    print(u)

square()
"""""""""""