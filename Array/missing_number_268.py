# first solution

def missingNumber(nums):
    nums.sort()
    n=len(nums)
    for i in range(n):
        if i !=nums[i]:
            return i
    return n

# second solution

def missingNumber(nums):
    return sum(range(len(nums)+1))-sum(nums)

print(missingNumber([0]))
# print(missingNumber([3,0,1]))
# print(missingNumber([0,1]))
# print(missingNumber([9,6,4,2,3,5,7,0,1]))