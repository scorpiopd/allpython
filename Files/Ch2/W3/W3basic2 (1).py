#Write a Python function that takes a sequence of
#numbers and determines whether all the numbers are different from each other.

num=["hat","mat","bat","bat"]


check=set(num)

if len(num) == len(check):
    print("No duplicates found")

else:
    print("Duplicates Found")