#!/usr/bin/python3
""" Define a square with a private instance attribute """


class Square:
    """Definition of the square"""
    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
