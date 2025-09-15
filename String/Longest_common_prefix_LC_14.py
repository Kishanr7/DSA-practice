# Algorithm Explanation:
# Problem: Given a list of strings, find the longest common prefix shared by all strings.
# Approach:
# 1. Find the length of the shortest string in the list (since the common prefix can't be longer than this).
# 2. Iterate through each character position up to the minimum length:
#    - For each position, check if all strings have the same character at that position.
#    - If a mismatch is found, return the prefix up to that position.
# 3. If no mismatch is found, return the prefix up to the minimum length.

def longestcommonprefix(strs):
    min_length=float('inf')
    for s in strs:
        if len(s) < min_length:
            min_length = len(s)
    i=0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i+=1
    return s[:i]
        
strs = ["flower","flow","flight"]
print(longestcommonprefix(strs))