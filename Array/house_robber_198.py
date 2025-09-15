# Algorithm Explanation:
# Problem: Given a list of non-negative integers representing the amount of money in each house, 
# find the maximum amount you can rob without robbing two adjacent houses.
# Approach:
# 1. Use dynamic programming to keep track of the maximum money that can be robbed up to each house.
# 2. For each house, you can either:
#    - Skip robbing it and take the max from the previous house.
#    - Rob it and add its value to the max from two houses before.
# 3. The recurrence relation is: dp[i] = max(dp[i-1], nums[i] + dp[i-2])
# 4. Initialize dp[0] and dp[1] with the first and max of first two house values.
# 5. Iterate through the houses and fill the dp array.
# 6. The answer is the last value in the dp array.

def rob(nums):
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

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

