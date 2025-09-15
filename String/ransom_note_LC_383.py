# Algorithm Explanation:
# Problem: Given two strings, ransom and magazine, determine if ransom can be constructed from magazine.
# Each letter in magazine can only be used once in ransom.
# Approach:
# 1. Count the frequency of each character in both ransom and magazine using Counter.
# 2. For each character in ransom:
#    - Check if the character exists in magazine and if magazine has at least as many occurrences as needed.
#    - If all characters in ransom are sufficiently present in magazine, return True.
#    - Otherwise, return False.

from collections import Counter
def can_construct(ransom, magazine):
    char_count, ransom_dict = Counter(magazine), Counter(ransom)
    count = 0
    for char, occ in ransom_dict.items():
        if char in char_count.keys() and occ <= char_count[char]:
            count += 1
    if count == len(ransom_dict):
        return True
    else:
        return False        

ransom = 'aa'
magazine = 'aaan'
print(can_construct(ransom,magazine))