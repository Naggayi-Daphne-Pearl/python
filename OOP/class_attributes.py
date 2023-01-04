# class attributes 
"""Class attributes are variables defined inside a class definition and associated with the class itself"""

class Person:
    """This is a class attribute"""
    number_of_people = 0
    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("pearl")
print(Person.number_of_people)


