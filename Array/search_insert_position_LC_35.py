# Algorithm Explanation:
# Problem: Given a sorted array and a target value, find the index if the target is found. 
# If not, return the index where it would be inserted in order.
# Approach:
# 1. Use binary search to efficiently find the target or its insert position.
# 2. Initialize left (l) and right (r) pointers to the start and end of the array.
# 3. While left <= right:
#    - Calculate mid index.
#    - If nums[mid] < target, move left pointer to mid + 1.
#    - If nums[mid] > target, move right pointer to mid - 1.
#    - If nums[mid] == target, return mid (target found).
# 4. After the loop, determine the correct insert position based on the last mid value.

def search_insert(nums, target):
    l = 0
    n = len(nums)
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    if nums[mid] < target:
        return mid + 1
    else:
        return mid

nums = [1, 3]
target = 2

print(search_insert(nums, target))