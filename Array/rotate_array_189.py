def rotate(nums, k):
    k = k % len(nums)  # Handle cases where k is greater than the length of the array
    nums[:] = [*nums[-k:], *nums[:-k]]
        
    return nums


nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))  # Output: [5,6,7,1,2,3,4]
