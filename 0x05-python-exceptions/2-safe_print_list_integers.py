#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for num in range(x):
        try:
            print("{:d}".format(mu_list[num]), end="")
            count = count + 1
        except ValueError:
            continue
    print("")
    return (count)
