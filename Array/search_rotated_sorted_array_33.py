# Algorithm Explanation:
# Problem: Given a rotated sorted array and a target value, find the index of the target if it exists, otherwise return -1.
# Approach:
# 1. Iterate through each element in the array.
# 2. If the current element equals the target, return its index.
# 3. If the target is not found after checking all elements, return -1.

def search(nums,target):
    for i in nums:
        if i==target:
            return nums.index(i)
    return -1

print(search([4,5,6,7,0,1,2],3))