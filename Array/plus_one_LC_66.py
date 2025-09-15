# Algorithm Explanation:
# Problem: Given a list of digits representing a non-negative integer, add one to the integer and return the result as a list of digits.
# Approach:
# 1. Convert the list of digits to a string, then to an integer.
# 2. Add one to the integer.
# 3. Convert the result back to a string, then split it into a list of digits.
# 4. Return the new list of digits.

def plus_one(digits):
    string_num = int(''.join(map(str, digits))) + 1
    return [int(i) for i in str(string_num)]
    
digits=[9]
print(plus_one(digits))