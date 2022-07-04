#!/usr/bin/python3
"""
Task 11 - Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ Initializer """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Calculates the area """
        return self.__size * self.__size

    def __str__(self):
        """ String Representation """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
