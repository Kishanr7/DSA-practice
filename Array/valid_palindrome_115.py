# Algorithm Explanation:
# Problem: Determine if a string is a valid palindrome, considering only alphanumeric characters and ignoring case.
# Approach:
# 1. Filter the string to keep only alphanumeric characters (letters and numbers) using isalnum().
# 2. Convert all characters to lowercase to make the comparison case-insensitive.
# 3. Compare the cleaned string with its reverse to check if it's a palindrome.
# 4. Return True if the string reads the same forwards and backwards, False otherwise.

def isPalindrome(s):
    # Step 1 & 2: Filter alphanumeric characters and convert to lowercase
    # isalnum() returns True for letters (a-z, A-Z) and digits (0-9)
    # This removes spaces, punctuation, and special characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Step 3: Compare the cleaned string with its reverse using slicing [::-1]
    # If they are equal, it's a palindrome
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))  # True