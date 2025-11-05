def wordPattern(pattern,s):
    hash_map = {}
    seen_values = []
    words=s.split()
    if len(pattern) != len(words):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in hash_map.keys():
            if words[i] in seen_values:
                return False
            hash_map[pattern[i]] = [words[i]]
            seen_values.append(words[i])
        elif pattern[i] in hash_map.keys() and words[i] in hash_map[pattern[i]]:
            continue
        else:
            hash_map[pattern[i]].append(words[i])
            seen_values.append(words[i])
    # print(hash_map.values())
    return all(isinstance(v, list) and len(v) == 1 for v in hash_map.values())
            
pattern = "aaa"
s = "aa aa aa aa"
print(wordPattern(pattern,s))