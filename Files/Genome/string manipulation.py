
def check(s1,s2):
    i=0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i+=1
    return s1[:i]
print(check("ACCATGT","ACCAGAC"))



import random

seq=[]
for i in range(10):
    seq+=random.choice('ACATERQK')
print(seq)
