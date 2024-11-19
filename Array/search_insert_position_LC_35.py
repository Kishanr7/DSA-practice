def search_insert(nums, target):
    l=0
    n=len(nums)
    r=n-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]<target:
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            return mid
    if nums[mid] < target:
        return mid+1
    else:
        return mid
            
nums=[1,3]
target=2

print(search_insert(nums,target))