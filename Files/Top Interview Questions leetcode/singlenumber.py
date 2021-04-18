Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
  
  
#solutions

#1   5600ms
for i in nums:
    if nums.count(i) ==1:
        print(i)

      

#2
 nums = collections.Counter(nums)
        
        for number, frequency in nums.items():
            if frequency == 1:
                return number
 
#3 best approach
 result = nums[0]
        
        for index in range(1, len(nums)):
            result ^= nums[index]
        
        return result







#4
numDict = set()
        for num in nums:
          if num in numDict:
            numDict.remove(num)
          else:
            numDict.add(num)



#5 SP
 nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return (nums[i])
        
        return (nums[-1])









#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
