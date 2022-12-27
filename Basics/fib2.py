# Adding memoization to the function easily
# The lru_cache decorator is used to add memoization to a function.
from functools import lru_cache

@lru_cache(maxsize = 200)
def fibonacci(n):
    #Error message for non integers
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be greater than 0")

    #Computing the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
        
for n in range(1, 101):
    print(n, ":", fibonacci(n))

# Error message for value not equal to int 
print(fibonacci(-1))

