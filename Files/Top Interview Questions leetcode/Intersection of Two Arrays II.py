
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.








a=[]
for i in nums1:
    if i in nums2:
        a.append(i)
        j=nums2.index(i)
        nums2[j]=-1
print(a)
        

 #sol2
d={}
a=[]
for i in nums1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for i in nums2:
    if i in d:
        if d[i]> 0:
            ar.append(i)
            d[i]-=1
print(a)



#sol3
def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())
  
  
  
