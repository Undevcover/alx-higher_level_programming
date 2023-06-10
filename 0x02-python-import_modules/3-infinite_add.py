#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0

    for index, num in enumerate(argv):
        if (index > 0):
            sum = sum + int(num)
    print("{:d}".format(sum))
