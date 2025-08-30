def rob_linear(nums):
    n = len(nums)

    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    return dp[n-1]

def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

