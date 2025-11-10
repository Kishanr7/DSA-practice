# Algorithm Explanation:
# Problem: Given a string s consisting of words and spaces, return the length of the last word in the string.
# Approach:
# 1. Remove any leading and trailing spaces from the string using strip().
# 2. Split the string into a list of words using split(" ").
# 3. Get the last word from the list.
# 4. Return the length of the last word.

def length_of_last_word(s):
    # striped_array = s.strip().split(" ")
    # length_of_array = len(striped_array)
    
    # return len(striped_array[length_of_array-1])
    # code without split and strip
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
print(length_of_last_word(s))