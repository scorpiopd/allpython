array =[2,8,3,9,1,6]


def inserionsort(array):
    for i in range(len(array)):
        j=i
        while j > 0 and array[j] < array[j-1]:
            swap(j,j-1,array)

            j-= 1
    return array
def swap(i,j,array):
    array[i],array[j]=array[j],array[i]


print(inserionsort(array))