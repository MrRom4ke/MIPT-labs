def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

print(fib(7))
