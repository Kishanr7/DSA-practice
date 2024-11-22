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