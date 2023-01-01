# Create a list of squares of the numbers 1 to 10 
squares = [x**2 for x in range(1,11)]
print (squares) # Output [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Create a list of even squares from 1 to 10 
even_squares = [x ** 2 for x in range(1,11) if x % 2 == 0]
print(even_squares) # Output [4, 16, 36, 64, 100]