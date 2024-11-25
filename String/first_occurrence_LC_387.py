def first_occurrence(s):
    h_map={}
    for char in s:
        if char in h_map:
            h_map[char] +=1
        else:
            h_map[char] =1
    print(h_map)
    for index, char in enumerate(h_map):
        if h_map[char] == 1:
            return s.index(char)
    return -1
#s="leetcode"
#s="loveleetcode"
#s="aavv"
#s="vd"
s="dddccdbba"
print(first_occurrence(s))