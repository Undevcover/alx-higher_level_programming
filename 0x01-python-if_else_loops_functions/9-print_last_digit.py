#!/usr/bin/python3
def print_last_digit(number: int) -> int:
    if number < 0:
        number = abs(number)
    last_digit = number % 10
    print(f"{last_digit}", end='')
    return (last_digit)
