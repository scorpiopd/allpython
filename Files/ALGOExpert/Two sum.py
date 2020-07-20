"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
"""

nums = [2, 7, 11, 15]
target = 18
"""def twosums(nums):

    for i in range(len(nums)):
        firstnum=nums[i]
        for j in range(i+1,len(nums)):
            secondnum=nums[j]
            if target==firstnum+secondnum:
                #return nums.index(firstnum),nums.index(secondnum)
                return [firstnum,secondnum]
            return []
print(twosums(nums))"""


#solution 2

"""def twosums(nums,target):
    ht={}
    for num in  nums:
        potentialmatch = target-num
        if potentialmatch in nums:
            return potentialmatch,num

        else   :

            ht= nums[num]

    return

print(twosums(nums,target))
"""

def twosums(nums,target):
    nums.sort()

    left=0
    right=len(nums) - 1

    while left < right:
        currentsum=nums[left] + nums[right]
        if currentsum ==target:
            return [nums[left],nums[right]]
        elif currentsum < target:
            left+=1
        elif currentsum > target:
            right-=1

    return []
print(twosums(nums,target))