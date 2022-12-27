raw_input= input("Please enter your name:  ")
if len(raw_input) < 6:
    print("Characters should have 6 characters.")

#check if a number is odd or even
interger = input("Enter interger: ")
number = int(interger)

if number % 2 == 0:
    print("The number is even.")
    
else:
    print("The number is odd.")

#Check sides of a triangle 
#1. Scalene triangle: All sides have different length 
#2. Isoceles triangle: Two sides have same length
#3. Equilateral triangle: All sides are equal 

a = input("Side a =  ")
b = input("Side b = ")
c = input("Side c = ")

if a != b and b != c and a != c :
    print('This is a scalene triangle.')
elif a == b and b == c : 
    print('This is an Equilateral triangle.')
else:
    print('This is an Isoceles triangle.')




