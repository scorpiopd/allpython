values=[8,9,2,4,1,0]
k=3


def partion(values,k):
    low=0
    high=len(values)-1

    i = 0
    while i<=high:
        n = values[i]

        if n > high:
            values[high],values[i]= values[i] ,values[high]
            high-=1
        if n < high:
            values[low],values[i] = values[i], values[low]
            low +=1
            i+=1
        if n==k:
            i+=1

    return values
print(partion(values,k))



""""+++++++++++++++++++++++++++++++++++++
a=[]
b=[]
def partion(values,k):
 for i in values:
    if i < k:
        a.append(i)
    else:
        i > k
        b.append(i)
 return a+b
print(partion(values,k))

"""