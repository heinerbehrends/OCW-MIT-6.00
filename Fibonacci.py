def fib(x):
    """return fibonacci of x where x is a non-negative integer."""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
print fib(4)
