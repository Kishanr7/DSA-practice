def find_the_difference(s, t):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    i=0
    j=len(sorted_s)-1
    while i<=j:
        if sorted_t[i] == sorted_s[i]:
            i+=1
        elif sorted_t[i] != sorted_s[i]:
            return sorted_t[i]
    return sorted_t[i]
s="avcd"
t="avcde"
print(find_the_difference(s,t))