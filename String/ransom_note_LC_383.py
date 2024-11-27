from collections import Counter
def can_construct(ransom, magazine):
    char_count, ransom_dict =Counter(magazine), Counter(ransom)
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