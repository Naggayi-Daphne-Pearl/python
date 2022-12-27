example = set()
example.add(42)
example.add(False)
example.add("Daphne")

print(example)


# Does not contain duplicate values
my_set = set([1, 2, 3, 3, 4, 4, 4])
print(my_set) 

# Add an element
my_set.add(5)
print(my_set)

# Remove an element
my_set.remove(1)
print(my_set)
#OR
my_set.discard(10)
print(my_set)



# Test membership
print(5 in my_set)  
print(1 in my_set)

# Take the union of two sets
other_set = {3, 4, 5, 6, 7, 8}
union_set = my_set | other_set
print(union_set)

# Take the intersection of two sets
intersection_set = my_set & other_set
print(len(intersection_set))

#Remove all elements
my_set.clear()
print(my_set)