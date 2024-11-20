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