array = 2, 4, 6, 7, 8, 9, 15, 17
target = 1


"""def binarysearch(array, target):
  return binarySearchHelper(array,target,0,len(array)-1)


def binarySearchHelper(array,target,left,right):
    if left > right :
        return -1
    middle=(left+right)//2
    potentialmatch=array[middle]
    if target == potentialmatch:
        return middle
    elif target < potentialmatch:
        return binarySearchHelper(array,target,left,middle-1)
    else:
        return binarySearchHelper(array,target,middle+1,right)


print(binarysearch(array,target))
"""

left=0
right=len(array) -1

def binarysearch(array,target,left,right):
    while left <= right :
        middle=(left+right)//2
        potentialmatch=array[middle]
        if target == potentialmatch:
            return middle
        elif target < potentialmatch:
            right=middle-1
        else:
            left=middle+1
    return -1

print(binarysearch(array,target,left,right))

