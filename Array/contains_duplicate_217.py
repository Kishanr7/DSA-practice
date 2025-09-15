# Algorithm Explanation:
# Problem: Given an array, determine if any value appears at least twice.
# Approach:
# 1. Initialize an empty set to keep track of seen numbers.
# 2. Iterate through each number in the array:
#    - If the number is already in the set, return True (duplicate found).
#    - Otherwise, add the number to the set.
# 3. If no duplicates are found after checking all numbers, return False.

def containsDups(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

#print(containsDups([1,2,3,1]))
print(containsDups([1,2,3,4]))
