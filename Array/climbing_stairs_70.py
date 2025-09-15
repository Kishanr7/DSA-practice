# Algorithm Explanation:
# Problem: Given n stairs, you can climb 1 or 2 stairs at a time. Find the number of distinct ways to reach the top.
# Approach:
# 1. If n == 1 or n == 2, return n (base cases).
# 2. Use dynamic programming to store the number of ways to reach each stair.
# 3. For each stair i from 3 to n:
#    - The number of ways to reach i is the sum of ways to reach (i-1) and (i-2).
#    - This is because you can reach stair i from either (i-1) by taking 1 step or from (i-2) by taking 2 steps.
# 4. Return the number of ways to reach the nth stair.

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climbStairs(5))  # Output: 8
print(climbStairs(6))  # Output: 13
print(climbStairs(7))  # Output: 21

