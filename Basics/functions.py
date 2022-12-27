import math


def f():
    # he pass statement is a null operation, which means it does nothing.  It is used as a placeholder in situations where a statement is required syntactically, but no action is needed.
    pass


# calling function
f()


def ping():
    return "Ping!!"


ping()


# Volume for a sphere
x = math.pi


def volume(r):
    v = (4.0 / 3.0) * x * r**3
    print(v)


volume(2)


# Area of a triangle : with two arguments
def triangle(b, h):
    print(0.5 * b * h)


triangle(3, 4)

# Keyword arguments: conversion of inch to meters
# Assign default arguments 0 to inches


def cm(inches=0, feet=0):
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 3.0
    print(inches_to_cm + feet_to_cm)
cm(inches = 5, feet=3)
cm(inches = 3)
