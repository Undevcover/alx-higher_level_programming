#!/usr/bin/python3
for letter in range(122, 96, -1):
    tmp = 0
    if letter % 2:
        tmp = 32
        order = chr(letter - tmp);
    print('{:s}'.format(order), end='')
