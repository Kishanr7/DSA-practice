# Algorithm Explanation:
# Problem: Determine if a number is a "happy number". A happy number is defined as:
# - Starting with any positive integer, replace the number by the sum of the squares of its digits.
# - Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle that does not include 1.
# - Those numbers for which this process ends in 1 are happy numbers.
# Approach:
# 1. Use a set to track numbers we've already seen to detect cycles.
# 2. While the number is not 1 and we haven't seen this number before:
#    - Add the current number to our seen set.
#    - Calculate the sum of squares of its digits and update n.
# 3. If we exit the loop because n == 1, it's a happy number (return True).
# 4. If we exit because n is in seen set, we've detected a cycle (return False).

def isHappy(n):
    seen = set()  # Track numbers we've already processed to detect cycles
    
    # Continue until we reach 1 (happy) or detect a cycle (not happy)
    while n != 1 and n not in seen:
        seen.add(n)  # Add current number to seen set
        
        # Calculate sum of squares of digits
        # Convert n to string, iterate through each digit, square it, and sum
        n = sum(int(digit) ** 2 for digit in str(n))
    
    # Return True if we reached 1 (happy number), False if we detected a cycle
    return n == 1

print(isHappy(19))  # Output: True
print(isHappy(2))   # Output: False