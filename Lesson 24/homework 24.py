def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib))
print(next)

def factorials():
    n = 1
    factorial = 1
    while True:
        yield factorial
        n += 1
        factorial *= n

for factorial in factorials():
    if factorial > 100:
        break
    print(factorial)