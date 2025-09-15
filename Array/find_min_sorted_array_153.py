# Algorithm Explanation:
# Problem: Given a rotated sorted array, find the minimum element.
# Approach:
# 1. Initialize a variable min_n to infinity to keep track of the minimum value found.
# 2. Iterate through each element in the array:
#    - If the current element is less than min_n, update min_n.
# 3. After checking all elements, return min_n as the minimum value in the array.

def findMin(nums):
    min_n = float('inf')
    for i in nums:
        if i < min_n:
            min_n = i
    return min_n

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))