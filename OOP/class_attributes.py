# class attributes


class Person:
    """Class attributes are variables defined inside a class definition and associated with the class itself
    Class attribute can be used to create a constant value within a class eg setting a constant for gravity i.e Gravity = 9.8"""
    """This is a class attribute"""
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    """- Class Methods: denoted with @classmethod
        - They act on the class itself. Dont have a class instance
        - cls references the class
    """
    @classmethod
    def number_of_person(cls):
        return cls.number_of_people()

    @classmethod 
    def add_person(cls):
        cls.number_of_people += 1



p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("pearl")
print(Person.number_of_people)

# class method
print(Person.number_of_person())