def search(nums,target):
    for i in nums:
        if i==target:
            return nums.index(i)
    return -1

print(search([4,5,6,7,0,1,2],3))