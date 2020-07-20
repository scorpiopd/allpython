#Write a Python program to create the combinations of 3 digit combo.


import random
n=''
for i in range(3):

    n=random.choice('234')

    print(n,end='')