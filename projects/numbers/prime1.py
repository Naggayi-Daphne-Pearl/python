def is_prime(n): 
    """Return 'True' if n is prime. False otherwise"""
    if n == 1:
        return False
    
    for d in range(2,n):
        if n % d == 1:
            return True # 1 is prime
        return False 
    
for n in range(1,23):
    print(n, is_prime(n))

