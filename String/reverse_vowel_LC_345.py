# Algorithm Explanation:
# Problem: Given a string, reverse only the vowels in the string.
# Approach:
# 1. Use two pointers: i starting from the beginning, j from the end of the string.
# 2. Convert the string to a list to allow swapping characters.
# 3. While i <= j:
#    - If l1[i] is a vowel, check l1[j]:
#        - If l1[j] is also a vowel, swap l1[i] and l1[j], then decrement j.
#        - If l1[j] is not a vowel, decrement j and continue.
#    - If l1[i] is not a vowel, increment i.
# 4. After processing, join the list back into a string and return it.

def reverse_vowel(s):
    i = 0
    j = len(s)-1
    l1=list(s)
    while i<=j:
        if l1[i].lower() in ['a','e','i','o','u']:
            if l1[j].lower() in ['a','e','i','o','u']:
                l1[i],l1[j] = l1[j],l1[i]
                j-=1
            else:
                j-=1
                continue
        i+=1
    return ''.join(map(str,l1))
    
s="IceCreAm"
s="leetcode"
print(reverse_vowel(s))