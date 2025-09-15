# Algorithm Explanation:
# Problem: Given two strings haystack and needle, find the index of the first occurrence of needle in haystack. Return -1 if needle is not part of haystack.
# Approach:
# 1. Use two pointers i (for haystack) and j (for needle).
# 2. Iterate through haystack and needle:
#    - If characters match, increment both pointers.
#    - If characters do not match, reset j to 0 and increment i.
#    - If j reaches the length of needle, return the starting index (i - j).
# 3. After the loop, if j equals the length of needle, return i - j (found); otherwise, return -1 (not found).

def strstr(haystack, needle):
    i=0
    j=0
    n=len(haystack)
    m=len(needle)
    while i < n and j < m:
        if haystack[i] != needle[j]:
            i+=1
            j=0
        elif haystack[i] == needle[j]:
            i+=1
            j+=1
        elif j == m:
            return i - j
        
    if j == m:
        return i-j
    else:
        return -1
    
'''haystack = "sadbutsad"
needle = "sad"
haystack = "leetcode"
needle = "leeto"'''

haystack = "mississippi"
needle = "issip"
print(strstr(haystack,needle))