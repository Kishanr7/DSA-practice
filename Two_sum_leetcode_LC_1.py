def twoSum(nums, target):
    while len(nums):
        ze=nums.pop()
        if target-ze in nums:
            print(len(nums))
            return [nums.index(target-ze), len(nums)]

'''def twoSum(nums,target):
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return i,j'''
            
            
print(twoSum([1, 3, 2,7,11,15],9))