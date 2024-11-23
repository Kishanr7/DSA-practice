def can_construct(ransom, magazine):
    char_count={}
    ransom_dict = {char:ransom.count(char) for char in ransom }
    print(ransom_dict)
    for char in magazine:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    count=0
    for char,occ in ransom_dict.items():
        if char in char_count.keys() and occ <=char_count[char]:
            count+=1
    if count == len(ransom_dict):
        return True
    else:
        return False        
    
ransom = 'aa'
magazine = 'aaan'
print(can_construct(ransom,magazine))