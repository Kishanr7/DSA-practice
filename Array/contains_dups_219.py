# Algorithm Explanation:
# Problem: Given an integer array nums and an integer k, return true if there are two distinct indices i and j 
# in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Approach:
# 1. Use a dictionary to store the most recent index of each number we've seen.
# 2. Iterate through the array with index i:
#    - If the current number exists in the dictionary, check if the distance between current index and stored index is <= k.
#    - If yes, return True (found nearby duplicate).
#    - Update the dictionary with the current index for this number (overwrite previous index).
# 3. If no nearby duplicates are found after checking all elements, return False.

def containsNearbyDuplicate(nums, k):
    num_dict = {}  # Dictionary to store number -> most recent index mapping
    n = len(nums)
    
    for i in range(n):
        # Check if we've seen this number before
        if nums[i] in num_dict:
            # Calculate distance between current index and previous occurrence
            if abs(num_dict[nums[i]] - i) <= k:
                return True  # Found nearby duplicate within distance k
        
        # Update/store the current index for this number
        num_dict[nums[i]] = i   
    
    return False  # No nearby duplicates found

# Test cases:
# print(containsNearbyDuplicate([1,2,3,1],3))     # True: indices 0 and 3, distance = 3 <= 3
print(containsNearbyDuplicate([1,0,1,1],1))       # True: indices 2 and 3, distance = 1 <= 1
print(containsNearbyDuplicate([1,2,3,1,2,3],2))   # False: nearest duplicates are distance 3 > 2