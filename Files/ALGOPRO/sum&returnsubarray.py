array=[1,3,2,5,7,2]
n=14

def sum(array,n):
    for start in range(len(array)):
        sum=0
        for end in range(start,len(array)):
            sum +=array[end]
            if sum ==n:
                return array[start:end+1]

    return None

print(sum(array,n))
