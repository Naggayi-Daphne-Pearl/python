# Using the [] operator
my_list = [1, 2, 3, 4]
print(my_list)  

# Using the list() function
my_list = list([1, 2, 3, 4])
print(my_list)  

# You can access the elements of a list by their index, which is the position of the element in the list. 
print(my_list[0])  # Output: 1
print(my_list[1])  # Output: 2
print(my_list[2])  # Output: 3
print(my_list[3])  # Output: 4

#You can also use negative indices to access the elements of a list from the end. The index of the last element is -1, the index of the second-to-last element is -2, and so on.
print(my_list[-1])  # Output: 4
print(my_list[-2])  # Output: 3
print(my_list[-3])  # Output: 2
print(my_list[-4])  # Output: 1


# Sorting Lists 

# Add an element
#append() method is a function that is used to add an element to the end of a list
my_list.append(5)
print(my_list)  # Output: [3, 2, 4, 1, 5]

# Remove an element
my_list.remove(2)
print(my_list)  # Output: [3, 4, 1, 5]

# Sort the list
# the sort() method is a function that is used to sort the elements of a list in ascending order
my_list.sort()
print(my_list)   # Output: [1, 3, 4, 5]

# #Descending order
# my_list.sort(reverse=True)
# print(my_list) # Output: [5,4,3,1]


#Slicing list
my_list [0:2]
print(my_list) # Output: [


#Combining lists 
letters = ['a', 'b', 'c', 'd', 'e']
x = letters + my_list
print(x) # Output: [ a, b, c, d, e, 1,3,4,5,]