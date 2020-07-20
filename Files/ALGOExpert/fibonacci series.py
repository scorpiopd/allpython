n=6

#solution 1
"""
from datetime import datetime
start_time = datetime.now()
def fibonacci(n):
    if n ==2:
        return 1
    elif n==1:
        return 0
    else :
        return  fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))

end_time = datetime.now()


print(f"Duration: {(end_time - start_time)}")


#time check program soultion 2
import time
start_time = time.time()
def fibonacci(n):
    if n ==2:
        return 1
    elif n==1:
        return 0
    else :
        return  fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))
print("--- %s seconds ---" % (time.time() - start_time))"""








#solution2
"""from datetime import datetime
start=datetime.now()
def fibonacci(n,memoize={1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n]=fibonacci(n-1,memoize) + fibonacci(n-2,memoize)
        return memoize[n]

print(fibonacci(n))
end=datetime.now()

print(F"DURATION {end-start}")"""
from datetime import datetime
start=datetime.now()
def getfib(n):
    lasttwo=[0,1]
    counter=3
    while counter  <=n:
        nextfib=lasttwo[0]+lasttwo[1]
        lasttwo[0]=lasttwo[1]
        lasttwo[1]=nextfib
        counter+=1

    return lasttwo[1]


print(getfib(n))
end=datetime.now()
print(f" Duration {end-start}")