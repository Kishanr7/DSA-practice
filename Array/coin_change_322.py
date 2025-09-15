# Algorithm Explanation:
# Problem: Given coins of different denominations and a total amount, find the minimum number of coins needed to make up that amount.
# Approach:
# 1. Use dynamic programming to build up the solution for all amounts from 1 to the target amount.
# 2. For each amount i from 1 to amount:
#    - For each coin, check if it can be used (i - coin >= 0).
#    - If yes, update the minimum coins needed for amount i by considering dp[i - coin] + 1.
# 3. Store the minimum coins needed for each amount in the dp array.
# 4. If dp[amount] is still infinity, return -1 (amount cannot be formed); otherwise, return dp[amount].

def coinChange(coins, amount):
    coins.sort()
    dp = [0] * (amount + 1)
    for i in range(1,amount+1):
        minn = float('inf')
        for coin in coins:
            diff = i - coin
            if diff < 0:
                break
            minn = min(minn, dp[diff] + 1)
        dp[i] = minn
    if dp[amount] < float('inf'):
        return dp[amount]
    else:
        return -1
print(coinChange([1,2,5], 11))  # Output: 3