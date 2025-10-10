# 392. Is Subsequence

def isSubsequence(s, t):
    # Edge case: empty string is always a subsequence
    if len(s) == 0:
        return True
    
    i = 0
    for j in range(len(t)):
        # Check if we still have characters to match in s
        if i < len(s) and s[i] == t[j]:
            i += 1
            # If we've matched all characters in s, return True early
            if i == len(s):
                return True
    
    # If we've gone through all characters in s, it's a subsequence
    return i == len(s)

print(isSubsequence("", "ahbgdc"))    # Output: True
print(isSubsequence("abc", "ahbgdc")) # Output: True
print(isSubsequence("axc", "ahbgdc")) # Output: False