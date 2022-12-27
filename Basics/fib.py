# Computing values using Fibonacci sequences
# Memoization:
fibonnacci_cache = {}
def fibonnacci(n):
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonnacci(n-1) + fibonnacci(n-2)
        # Cache the value and return it
    fibonnacci_cache[n] = value 
    return value 
for n in range(1,1001):
    print(n, ":", fibonnacci(n))
    

# # This method slows down for long sequences.        
# for n in range (1,11) :
#     print(n, ":", fibonnacci(n))


