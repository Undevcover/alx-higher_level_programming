#!/usr/bin/python3
def print_last_digit(number:int)->int:
    if number < 0:
        return (10 - (number % 10))
    return (number % 10)
