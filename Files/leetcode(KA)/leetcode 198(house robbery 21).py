def rob(nums):
    if len(nums) == 0:
        return 0
    if len(nums) ==1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])

    max_loot=[nums[0],max(nums[0], nums[1])]

    for i in range(2,len(nums)):
        max_loot.append(max(nums[i] + max_loot[i-2],max_loot[i-1]))

    return max_loot.pop()

print(rob([2,7,9,3,1]))

