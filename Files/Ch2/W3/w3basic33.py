

num=input("enter a num")
b=list(map(int,num.split()))
print(b)



listOfElems = [b]
def checkIfDuplicates_1(listOfElems):

        if len(listOfElems) == len(set(listOfElems)):
            s=sum(listOfElems)
            return f"your sum of numbers is {s}"
        else:
            return ("entered duplicates")

print(checkIfDuplicates_1(b))