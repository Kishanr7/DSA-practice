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