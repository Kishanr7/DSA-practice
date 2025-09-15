# Algorithm Explanation:
# Problem: Given a string s, find the index of the first non-repeating character. If none exists, return -1.
# Approach:
# 1. Use Counter to count the frequency of each character in the string.
# 2. Iterate through the keys of the Counter (unique characters):
#    - If a character's count is 1, return its index in the string (first occurrence).
# 3. If no non-repeating character is found, return -1.

from collections import Counter
def first_occurrence(s):
    h_map=Counter(s)
    for char in h_map.keys():
        if h_map[char] == 1:
            return s.index(char)
    return -1
#s="leetcode"
#s="loveleetcode"
#s="aavv"
#s="vd"
s="dddccdbba"
print(first_occurrence(s))