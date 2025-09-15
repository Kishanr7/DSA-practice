# Algorithm Explanation:
# Problem: Given an array and a value, remove all instances of that value in-place and return the new length.
# Approach:
# 1. Use a pointer i to iterate through the array.
# 2. While i is less than the length of the array:
#    - If nums[i] equals the value to remove, pop it from the array (removes the element at index i).
#    - Else, increment i to check the next element.
# 3. The array is modified in-place, and all instances of the value are removed.

def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
            
nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element(nums,val))