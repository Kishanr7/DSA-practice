# Algorithm Explanation:
# Problem: Given two strings haystack and needle, find the index of the first occurrence of needle in haystack. Return -1 if needle is not part of haystack.
# Approach:
# 1. Use a brute force approach with nested loops to check every possible starting position in haystack.
# 2. For each starting position i in haystack:
#    - Initialize j = 0 to track position in needle
#    - Use inner loop with k starting from i to compare characters
#    - If haystack[k] matches needle[j], increment j to check next character in needle
#    - If characters don't match, break out of inner loop and try next starting position
#    - If j reaches the length of needle (j == m), we found a complete match, return starting index i
# 3. If no match is found after checking all positions, return -1

def strstr(haystack, needle):
    n = len(haystack)  # Length of haystack string
    m = len(needle)    # Length of needle string
    
    # Try each position in haystack as a potential starting point
    for i in range(n):
        j = 0  # Reset needle pointer for each new starting position
        
        # Check if needle matches starting from position i in haystack
        for k in range(i, n):
            if haystack[k] == needle[j]:
                j += 1  # Move to next character in needle
            else:
                break   # Characters don't match, try next starting position
            
            # If we've matched all characters in needle, return starting index
            if j == m:
                return i
    
    return -1   # Needle not found in haystack

# Test cases
# haystack = "sadbutsad"    # Expected: 0 (needle "sad" found at index 0)
# needle = "sad"
# haystack = "leetcode"     # Expected: -1 (needle "leeto" not found)
# needle = "leeto"

haystack = "mississippi"
needle = "issip"
print(strstr(haystack,needle))  # Expected: 4 (needle "issip" found at index 4)