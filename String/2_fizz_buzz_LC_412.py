def fizz_buzz(n):
    c=[("FizzBuzz" if i % 5 == 0 and i % 3 == 0 else ( "Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else str(i)))) for i in range(1, n+1)]
    return c
n=15
print(fizz_buzz(n))