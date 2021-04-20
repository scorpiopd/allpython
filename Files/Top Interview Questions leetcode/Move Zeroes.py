
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]




  
nums = [0,1,0,3,12]

for i in range(1,len(nums)):
    if 0 in nums:
        nums.remove(0)
        nums.insert(len(nums),0)
print(nums)







#swap approach
nums = [0,1,0,3,12]

j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1
print(nums)
