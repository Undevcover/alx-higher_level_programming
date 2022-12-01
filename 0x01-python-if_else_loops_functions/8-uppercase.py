#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            cap = ord(i)-32
        print('{:s}'.format(chr(cap)), end='')
    print('')
