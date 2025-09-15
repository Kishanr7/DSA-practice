# Algorithm Explanation:
# Problem: Given an array of integers, find the contiguous subarray with the largest sum.
# Approach:
# 1. Use Kadane's Algorithm to efficiently find the maximum subarray sum.
# 2. Initialize max_sum to negative infinity and current_sum to 0.
# 3. Iterate through each number in the array:
#    - Add the current number to current_sum.
#    - Update max_sum if current_sum is greater than max_sum.
#    - If current_sum becomes negative, reset it to 0 (start a new subarray).
# 4. After checking all elements, return max_sum as the largest subarray sum.

def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(maxSubArray([-2,0,-1]))
