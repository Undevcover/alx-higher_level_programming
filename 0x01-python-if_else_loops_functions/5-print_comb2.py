#!/usr/bin/python3
for num in range(1, 100):
    if num <=98:
        print('{:02d}'.format(num), end=', ')
    else:
        print('{:02d}'.format(num), end='\n')
