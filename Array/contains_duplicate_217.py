def containsDups(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

#print(containsDups([1,2,3,1]))
print(containsDups([1,2,3,4]))
