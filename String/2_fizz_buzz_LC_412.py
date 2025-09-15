# Algorithm Explanation:
# Problem: Given an integer n, return a list of strings representing the numbers from 1 to n.
# For multiples of 3, add "Fizz" instead of the number.
# For multiples of 5, add "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, add "FizzBuzz".
# Approach:
# 1. Iterate through numbers from 1 to n.
# 2. For each number:
#    - If divisible by both 3 and 5, add "FizzBuzz".
#    - Else if divisible by 3, add "Fizz".
#    - Else if divisible by 5, add "Buzz".
#    - Else, add the number as a string.
# 3. Return the resulting list.

def fizz_buzz(n):
    c=[("FizzBuzz" if i % 5 == 0 and i % 3 == 0 else ( "Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else str(i)))) for i in range(1, n+1)]
    return c
n=15
print(fizz_buzz(n))