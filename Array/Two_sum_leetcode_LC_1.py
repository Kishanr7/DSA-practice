# Algorithm Explanation:
# Problem: Given an array of integers and a target value, find indices of the two numbers such that they add up to the target.
# Approach:
# 1. Iterate through the array by popping elements from the end.
# 2. For each popped element (ze), check if (target - ze) exists in the remaining array.
# 3. If found, return the indices of the two numbers:
#    - The index of (target - ze) in the remaining array.
#    - The current length of the array (which is the index of ze before it was popped).
# 4. Print and return the result when a valid pair is found.

def twoSum(nums, target):
    while len(nums):
        ze = nums.pop()
        if target - ze in nums:
            print(len(nums))
            return [nums.index(target - ze), len(nums)]
print(twoSum([1, 3, 2, 7, 11, 15], 9))