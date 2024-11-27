def fizz_buzz(n):
    c=[]
    for i in range(1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            c.append("FizzBuzz")
        elif i % 3 == 0:
            c.append("Fizz")
        elif i % 5 == 0:
            c.append("Buzz")
        else:
            c.append(f"{i}")
    return c

n=15
print(fizz_buzz(n))