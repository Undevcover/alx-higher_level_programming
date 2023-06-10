#!/usr/bin/python3
def main():
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
    for arg in argv:
        if (argv.index(arg) != 0):
            print("{}: {}".format(argv.index(arg), arg))
if __name__ == "__main__":
    main()
