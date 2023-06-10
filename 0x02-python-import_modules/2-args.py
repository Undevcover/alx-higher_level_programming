#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    punc = ":"

    if (length == 1):
        punc = "."
    if (length == 2):
        word = "argument"
    else:
        word = "arguments"
    print("{} {}{}".format(length - 1, word, punc))
    for index, arg in enumerate(argv):
        if (index != 0):
            print("{}: {}".format(argv.index(arg), arg))
