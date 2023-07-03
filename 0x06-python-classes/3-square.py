#!/usr/bin/python3
""" class Square that defines a square with a 
    private instace attribute __size
    and a public instance method area
"""


class Square:
    """definitiion of a square"""

    def __init__(self, size=0):
         """initializes a new square.
            Args:
                size (int): size of the new square
            """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area returns the area of the square, size * size """
        return (self.__size * self.__size)
