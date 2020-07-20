"""Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1"""

nums=2, 4, 6, 7, 8, 9, 15, 17
target=17
def searchinsert(nums,target):
    lo=0
    hi=len(nums)-1

    while lo<=hi:
        mid= (hi+lo)/2
        m=int(mid)


        midval = nums[m]
        if target == midval:
            return m
        elif target > midval:
            lo =m+1

        else:
            hi =m-1
    return lo

print(searchinsert(nums,target))

