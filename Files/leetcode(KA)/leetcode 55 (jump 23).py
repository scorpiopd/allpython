def canJump(nums):
    maxreach=0
    for currentstep in range(len(nums)):
        if currentstep > maxreach:
            return False
        currentreach = currentstep + nums[currentstep]
        maxreach =max(maxreach,currentreach)

    return True

print(canJump([3,2,1,0,4]))