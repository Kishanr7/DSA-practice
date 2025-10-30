def reverseWords(s):
    l = s.split()
    # print(l[::-1])
    return ' '.join(l[::-1])
    
    
s = "the sky is blue"
s = "  hello world  "
print(reverseWords(s))