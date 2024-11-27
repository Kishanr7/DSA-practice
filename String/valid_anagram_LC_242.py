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