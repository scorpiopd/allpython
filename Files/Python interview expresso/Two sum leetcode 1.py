"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""

nums=[3,7,2,15]
target = 9
def twosums(nums,target):
    for i,num in enumerate(nums):
        want= target - num
        for j,other in enumerate(nums[i:]):
            if other == want:
                return[i,j+1]

print(twosums(nums,target))


# solution 2

"""def twosums(target,nums):
    ht={}
    for i,num in enumerate(nums):
        want= target-num
        if want in ht:
            leftindex=ht[want]
            return [leftindex,i]
        else:
            ht[num]=i
print(twosums(target,nums))
"""