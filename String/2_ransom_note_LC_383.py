# Algorithm Explanation:
# Problem: Given two strings, ransom and magazine, determine if ransom can be constructed from magazine.
# Each letter in magazine can only be used once in ransom.
# Approach:
# 1. Create a hashmap (dictionary) for both ransom and magazine to count the occurrences of each character.
# 2. For each character in ransom's hashmap:
#    - Check if the character exists in magazine's hashmap and if magazine has at least as many occurrences as needed.
#    - If all characters in ransom are sufficiently present in magazine, return True.
#    - Otherwise, return False.

def can_construct(ransom, magazine):
    r_hash = create_hashmap(ransom)
    m_hash = create_hashmap(magazine)
    count=0
    print(r_hash, m_hash)
    for char,occ in r_hash.items():
        if char in m_hash.keys() and occ <=m_hash[char]:
            count+=1
    if count == len(r_hash):
        return True
    else:
        return False
    
def create_hashmap(s):
    char_count={}
    for char in s:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count  
    
ransom = 'aa'
magazine = 'aaan'
print(can_construct(ransom,magazine))