# Algorithm Explanation:
# Problem: Given an unsorted array of integers, find the length of the longest increasing subsequence.
# Approach:
# 1. Use dynamic programming to keep track of the length of the longest increasing subsequence ending at each index.
# 2. Initialize a dp array where dp[i] represents the length of the longest increasing subsequence ending at index i.
# 3. For each element nums[i], check all previous elements nums[j] (where j < i):
#    - If nums[i] > nums[j], update dp[i] to be the maximum of its current value and dp[j] + 1.
# 4. After processing all elements, the answer is the maximum value in the dp array.

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
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))            # Output: 4