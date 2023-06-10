#!/usr/bin/python3
from sys import argv

def main():
    length = len(argv) - 1
    punc = ":"
    if (length == 0):
        punc = "."
    if (length == 1):
        word = "arguement"
    else:
        word = "arguments"
    print("{} {}{}".format(length, word, punc))
    for arg in argv:
        if (argv.index(arg) != 0):
            print("{}: {}".format(argv.index(arg), arg))
if __name__ == "__main__":
    main()
~

