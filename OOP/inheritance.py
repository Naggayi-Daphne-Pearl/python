# Inheritance: 
class Pet: 
    """Inheritance method: Pet Class contains the functionality shared by the children classes
    Pet Class is a parent class """
    def __init__(self, name,age): 
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and {self.age} years old")


"""Class Cat and Dog have functions that are more specific and different from each other. 
These are child classes """
class Cat(Pet):
    """Calling a super class to iniate the super class"""
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print('Meow')
    def show(self):
        print(f"I am {self.name} and {self.age} years old and I color {self.color}") 
    

class Dog(Pet):
    def speak(self):
        print('Bark!')

# Intiante 
p = Pet('Pearl', 4)
p.show()
c = Cat('Bill', 13, 'green')
c.show()
c.speak()



