# Inheritance: 
class Pet: 
    """Inheritance method: Pet Class contains the functionality shared by the class Cat and Dog.
    Pet Class is a general class  """
    def __init__(self, name,age): 
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and {self.age} years old")


"""Class Cat and Dog have functions that are more specific and different from each other """
class Cat(Pet):
    def speak(self):
        print('Meow')

class Dog(Pet):
    def speak(self):
        print('Bark!')

p = Pet('Pearl', 4)
p.show()


