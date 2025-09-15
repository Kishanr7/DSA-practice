# Algorithm Explanation:
# Problem: Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.
# Approach:
# 1. Use two pointers: i to iterate through the array, j to track the position for the next unique element.
# 2. Start j at 1 since the first element is always unique.
# 3. For each element from index 1 to n-1:
#    - If the current element is not equal to the previous element, assign it to nums[j] and increment j.
# 4. After processing, j will be the length of the array with unique elements at the start.

def remove_duplicates(nums):
    n = len(nums)
    j = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
