# Algorithm Explanation:
# Problem: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one number that is missing.
# Approach:
# Solution 1:
# 1. Sort the array.
# 2. Iterate through the array and check if the value at each index matches the index.
#    - If a mismatch is found, return the index as the missing number.
# 3. If all indices match, return n (the last number is missing).
#
# Solution 2:
# 1. Calculate the expected sum of numbers from 0 to n using sum(range(n+1)).
# 2. Subtract the actual sum of the array from the expected sum to find the missing number.
# 3. Return the result.

# first solution

def missingNumber(nums):
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i != nums[i]:
            return i
    return n

# second solution

def missingNumber(nums):
    return sum(range(len(nums)+1)) - sum(nums)

print(missingNumber([0]))
# print(missingNumber([3,0,1]))
# print(missingNumber([0,1]))
# print(missingNumber([9,6,4,2,3,5,7,0,1]))