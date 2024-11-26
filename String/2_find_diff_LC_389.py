from collections import Counter
def find_the_difference(s, t):
    counter_s, counter_t = Counter(s), Counter(t)
    
    for c in counter_t:
        if c not in counter_s:
            return c
        if counter_s[c] < counter_t[c]:
            return c
    
s="avcd"
t="avcde"
print(find_the_difference(s,t))