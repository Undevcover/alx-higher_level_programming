#!/usr/bin/python3
for idx1 in range(0, 9):
    for idx2 in range(idx1 + 1, 10):
        if idx1 < 8:
            print("{:d}{:d}, ".format(idx1, idx2), end="")
        else:
            print("{:d}{:d}".format(idx1, idx2))
