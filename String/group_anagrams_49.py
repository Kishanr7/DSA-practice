def groupAnagrams(strs):
        # take a dictionary, 
    seen = {}
    l = []
    for i in strs:
        value = ''.join(sorted(i))
        if value not in seen.keys():
            seen[value] = [i]
        else:
            seen[value].append(i)
    print(seen.values(), type(seen.values()))
    for key, value in seen.items():
        l.append(value)
    return l
            
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))