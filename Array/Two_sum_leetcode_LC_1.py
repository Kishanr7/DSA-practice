def twoSum(nums, target):
    while len(nums):
        ze=nums.pop()
        if target-ze in nums:
            print(len(nums))
            return [nums.index(target-ze), len(nums)]
            
print(twoSum([1, 3, 2,7,11,15],9))