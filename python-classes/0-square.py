#!/usr/bin/python3
# Import the Square class
Square = __import__('0-square').Square
# Create a Square object
my_square = Square()
# Print the object type
print(type(my_square))
# Print the object's attributes
print(my_square.__dict__)
