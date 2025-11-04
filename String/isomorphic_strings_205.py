def isIsomorphic(s,t):
    hash_map = {}
    seen_values = []
    for i in range(len(s)):
        if s[i] not in hash_map.keys():
            if t[i] in seen_values:
                return False
            hash_map[s[i]] = [t[i]]
            seen_values.append(t[i])
        elif s[i] in hash_map.keys() and t[i] in hash_map[s[i]]:
            continue
        else:
            hash_map[s[i]].append(t[i])
            seen_values.append(t[i])
    # print(hash_map.values())
    return all(isinstance(v, list) and len(v) == 1 for v in hash_map.values())
            
s = "badc" 
t = "baba"
print(isIsomorphic(s,t))