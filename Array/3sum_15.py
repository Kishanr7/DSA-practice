# Algorithm Explanation:
# Problem: Given an array, find all unique triplets that sum to zero.
# Approach:
# 1. Sort the array to make it easier to avoid duplicates and use two pointers.
# 2. Loop through each number as the first element of the triplet.
#    - Skip duplicate first elements to avoid duplicate triplets.
# 3. For each first element, use two pointers (left and right) to find pairs that sum with the first element to zero.
#    - If the sum is zero, add the triplet to the result and move both pointers, skipping duplicates.
#    - If the sum is less than zero, move the left pointer right to increase the sum.
#    - If the sum is greater than zero, move the right pointer left to decrease the sum.
# 4. Continue until all unique triplets are found and return the result.

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    return result

# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))