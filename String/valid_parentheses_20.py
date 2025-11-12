# Algorithm Explanation:
# Problem: Given a string containing only the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. A string is valid if:
#  - Every opening bracket has a corresponding closing bracket of the same type.
#  - Brackets are closed in the correct order (well-nested).
#
# Approach (stack-based):
# 1. Use a dictionary (hash_map) that maps each closing bracket to its matching opening bracket.
# 2. Iterate through each character in the string:
#    - If the character is an opening bracket, push it onto the stack.
#    - If the character is a closing bracket:
#        a) If the stack is empty, there's no matching opening bracket -> invalid (return False).
#        b) Otherwise check the top of the stack:
#           - If the top element equals the expected opening bracket (hash_map[c]), pop it (match found).
#           - If it does not match, the brackets are mis-ordered or mismatched -> invalid (return False).
# 3. After processing all characters, the string is valid only if the stack is empty (all openings were matched).
#
# Time complexity: O(n), where n is length of s (each char pushed/popped at most once).
# Space complexity: O(n) in the worst case for the stack.

def isValid(s):
    hash_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stk = []
    for c in s:
        # If c is an opening bracket, push onto stack
        if c not in hash_map:
            stk.append(c)
        else:
            # c is a closing bracket: there must be a matching opening bracket on top of stack
            if not stk or stk[-1] != hash_map[c]:
                return False
            # matched, pop the opening bracket
            stk.pop()
    # valid if no unmatched opening brackets remain
    return not stk
s = "([)]"
print(isValid(s))