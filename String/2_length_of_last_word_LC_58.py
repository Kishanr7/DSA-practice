def length_of_last_word(s):
    i=len(s)-1
    if len(s) == 1 and s[0] != ' ':
        return 1
    while s[i] == ' ':
        i-=1
    counter = 0
    while s[i] != ' ' and i>=0:
        i-=1
        counter+=1
    return counter
    
    
s="fly me      to     the moon   "
s="hello world     "
s='day'
print(length_of_last_word(s))