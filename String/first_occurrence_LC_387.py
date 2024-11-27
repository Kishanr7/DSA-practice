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