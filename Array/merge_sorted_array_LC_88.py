# Algorithm Explanation:
# Problem: Given two sorted arrays nums1 and nums2, merge nums2 into nums1 as one sorted array in-place.
# Approach:
# 1. Use three pointers: x for the end of nums1's valid elements, y for the end of nums2, and z for the end of nums1's total length.
# 2. Start filling nums1 from the end (z) to avoid overwriting its valid elements.
# 3. Compare nums1[x] and nums2[y]:
#    - If nums1[x] > nums2[y], place nums1[x] at nums1[z] and move x backward.
#    - Else, place nums2[y] at nums1[z] and move y backward.
# 4. If nums2 still has elements left after nums1 is exhausted, copy them into nums1.
# 5. Return the merged array.

def merge(nums1,m,nums2,n):
    x, y = m-1, n-1
    for z in range(m+n-1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6] 
n = 3
print(merge(nums1,m,nums2,n))