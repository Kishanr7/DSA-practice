def remove_duplicates(nums):
    n=len(nums)
    j=1
    for i in range(1,n):
        if nums[i] != nums[i-1]:
            nums[j]=nums[i]
            j+=1
    return j

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(nums))
