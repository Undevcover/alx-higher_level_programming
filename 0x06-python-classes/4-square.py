#!/usr/bin/python3
"""class that access and update private attribute"""


class Square:
    """ Definition of sqaure class"""
    def __init__(self, size=0):
        """Initializes a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integert")
        elif value < 0:
            raise Valueerror("size must be >= o")
        self.__size = value

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)
