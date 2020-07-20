# Roman to decimal number
#algopro video number 62

def romantoint(s):
    romannumerals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    prev=0
    sum=0
    for i in s[::-1]:
        curr=romannumerals[i]
        #sum=sum+(-curr if prev>curr else  curr)
        if prev > curr:
            sum -=curr
        else:
            sum +=curr

        prev=curr


    return sum
n='MCMIV'
print(romantoint(n))