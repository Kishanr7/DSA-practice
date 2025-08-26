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
print(coinChange([1,2,5], 11))  # Output: 20