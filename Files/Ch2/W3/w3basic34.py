#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

fnum=int(input("enter first number"))
snum=int(input("enter second number"))


finalsum=fnum+snum

if finalsum > 15 and finalsum < 20:
    print (f"your sum is 20 ")

else:
    print(f"your sum is {finalsum} ")
"""
if finalsum  in range(15,20):
    print(" your sum is 20")

else:
    print(f"your sum is {finalsum}")"""