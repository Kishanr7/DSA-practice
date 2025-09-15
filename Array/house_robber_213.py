# Algorithm Explanation:
# Problem: Given a list of non-negative integers representing the amount of money in each house arranged in a circle,
# find the maximum amount you can rob without robbing two adjacent houses (first and last are also adjacent).
# Approach:
# 1. Since the first and last houses are adjacent, you cannot rob both.
# 2. Solve the problem twice using the standard House Robber algorithm:
#    - Case 1: Rob houses from the second to the last (exclude the first house).
#    - Case 2: Rob houses from the first to the second last (exclude the last house).
# 3. For each case, use dynamic programming:
#    - For each house, decide to rob it (add its value to the max from two houses before) or skip it (take max from previous house).
#    - The recurrence relation is: dp[i] = max(dp[i-1], nums[i] + dp[i-2])
# 4. Return the maximum result from both cases.

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

    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

