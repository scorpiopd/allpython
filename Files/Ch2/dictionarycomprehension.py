nums = dict(first=1,second=2,third=3)
squarednums= {key:value **2 for key,value in nums.items()}
print(squarednums)

a={num:num*2 for num in [1,2,3]}
print(a)

str1="ABC"
str2="123"
combo={str1[i]:str2[i]for i in range(0,len(str1))}
print(combo)1