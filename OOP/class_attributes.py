# class attributes 
"""Class attributes are variables defined inside a class definition and associated with the class itself"""

class Person:
    """This is a class attribute"""
    number_of_people = 8
    def __init__(self,name):
        self.name = name

p1 = Person("tim")
p2 = Person("pearl")
Person.number_of_people = 4
print(p2.number_of_people)
