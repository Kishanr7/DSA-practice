# Algorithm Explanation:
# Problem: Given a string s consisting of words and spaces, return the length of the last word in the string.
# Approach:
# 1. Remove any leading and trailing spaces from the string using strip().
# 2. Split the string into a list of words using split(" ").
# 3. Get the last word from the list.
# 4. Return the length of the last word.

def length_of_last_word(s):
    striped_array = s.strip().split(" ")
    length_of_array = len(striped_array)
    
    return len(striped_array[length_of_array-1])
    
    
s="fly me      to     the moon   "
print(length_of_last_word(s))