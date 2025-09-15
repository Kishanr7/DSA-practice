# Algorithm Explanation:
# Problem: Given a string s consisting of words and spaces, return the length of the last word in the string.
# Approach:
# 1. Start from the end of the string and skip any trailing spaces.
# 2. Initialize a counter to 0.
# 3. Iterate backwards through the string:
#    - For each non-space character, increment the counter.
#    - Stop when a space is encountered or the start of the string is reached.
# 4. Return the counter as the length of the last word.

def length_of_last_word(s):
    i = len(s) - 1
    if len(s) == 1 and s[0] != ' ':
        return 1
    while s[i] == ' ':
        i -= 1
    counter = 0
    while s[i] != ' ' and i >= 0:
        i -= 1
        counter += 1
    return counter
    
    
s = "fly me      to     the moon   "
s = "hello world     "
s = 'day'
print(length_of_last_word(s))