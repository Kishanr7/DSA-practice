def merge(nums1,m,nums2,n):
    x, y = m-1,n-1
    for z in range(m+n-1,-1,-1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x-=1
        else:
            nums1[z] = nums2[y]
            y-=1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
print(merge(nums1,m,nums2,n))