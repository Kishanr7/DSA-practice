def canJump(nums):
    n = len(nums)
    goal = n - 1
    
    for i in range(n - 1, -1, -1):
        max_jump = nums[i]
        if i + max_jump >= goal:
            goal = i
            
    if goal == 0:
        return True
    else:
        return False

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
# nums = [2,0]
print(canJump(nums))