
array=[2,5,67,8,9,1,3]
def bubblesort(array):
    issorted=False
    while not issorted:
        issorted =True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swap(i,i+1,array)
                issorted=False
    return array

def swap(i,j,array):
    array[i],array[j]=array[j],array[i]

print(bubblesort(array))