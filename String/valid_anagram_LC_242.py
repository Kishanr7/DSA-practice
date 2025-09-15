# Algorithm Explanation:
# Problem: Given two strings s and t, determine if t is an anagram of s (i.e., both strings contain the same characters with the same frequency).
# Approach:
# 1. Count the frequency of each character in both strings using Counter.
# 2. Compare the keys (unique characters) of both counters:
#    - If the sets of keys are not equal, return False.
# 3. For each character in t, check if its count matches in both strings:
#    - If any character count differs, return False.
# 4. If all checks pass, return True (strings are anagrams).

from collections import Counter
def is_anagram(s, t):
    #return sorted(s) == sorted(t)
    count_s, count_t = Counter(s), Counter(t)
    if count_s.keys() == count_t.keys():
        for i in count_t:
            if count_t[i]!=count_s[i]:
                return False
    else:
        return False
    return True

#s='anagram'
#t='nagaram'
#s='rat'
#t='car'
s='a'
t='av'
print(is_anagram(s,t))