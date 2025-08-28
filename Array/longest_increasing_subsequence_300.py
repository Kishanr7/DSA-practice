def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize the dp array with 1s

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))               # Output: 4