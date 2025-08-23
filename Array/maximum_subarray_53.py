def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 1
    
    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(maxSubArray([-2,0,-1]))
