def findMin(nums):
    min_n = float('inf')
    for i in nums:
        if i < min_n:
            min_n = i
    return min_n

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))