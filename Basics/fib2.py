# Adding memoization to the function easily
# The lru_cache decorator is used to add memoization to a function.
from functools import lru_cache

@lru_cache(maxsize = 200)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
        
for n in range(1, 101):
    print(n, ":", fibonacci(n))

