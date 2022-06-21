#!/usr/bin/python3
"""
Sample class for OOP project
"""


class Square:
    """ Square Class """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        return(self.area() == other.area())

    def __ne__(self, other):
        return(self.area() != other.area())

    def __gt__(self, other):
        return(self.area() > other.area())

    def __lt__(self, other):
        return(self.area() < other.area())

    def __le__(self, other):
        return(self.area() <= other.area())

    def __ge__(self, other):
        return(self.area() >= other.area())
