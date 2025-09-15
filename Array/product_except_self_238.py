# Algorithm Explanation:
# Problem: Given an array nums, return an array output such that output[i] is the product of all elements of nums except nums[i], without using division and in O(n) time.
# Approach:
# 1. Initialize an output array with 1s.
# 2. First pass (left to right): For each index, store the product of all elements to the left of that index.
#    - Use left_product to keep track of the running product from the left.
# 3. Second pass (right to left): For each index, multiply the output value by the product of all elements to the right of that index.
#    - Use right_product to keep track of the running product from the right.
# 4. The final output array contains the product of all elements except the one at each index.

def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    
    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]
    
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))