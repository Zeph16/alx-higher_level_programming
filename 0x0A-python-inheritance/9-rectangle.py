#!/usr/bin/python3
"""
Task 9 - Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        """ Initializer """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculates the area """
        return self.__width * self.__height

    def __str__(self):
        """ String representation """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
