def length_of_last_word(s):
    striped_array = s.strip().split(" ")
    length_of_array = len(striped_array)
    
    return len(striped_array[length_of_array-1])
    
    
s="fly me      to     the moon   "
print(length_of_last_word(s))