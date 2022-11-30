#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
preamble = f'Last digit of {number} is'
if (lastDigit != 0) and (lastDigit < 6):
    print(f'{preamble} {lastDigit} and is less than 6 and not 0')
elif lastDigit == 0:
    print(f'{preamble} {lastDigit} and is 0')
elif lastDigit > 5:
    print(f'{preamble} {lastDigit} and is greater than 5')
