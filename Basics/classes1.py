# Simple example for a class
class Dog:
    """Simple example for a class for a dog. 
    - The __init__ method is a simple method called when an object is created.  It is used to intialize the object's attributes.
    - The self method is used to refer to the current instance of an object in a class method. Similar to 'this' in other languages. """  
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woooff!!!")
    
# Create new Dog object. 
dog1 = Dog('Sam', 'German Sherpherd')
dog2 = Dog('Megahan', 'Sherpherd')

# print dogs's name and breed
#the object's attributes are accessed using the dot notation 
print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)
help(Dog)