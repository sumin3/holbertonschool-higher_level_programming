#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return (i + 1)
    except (IndexError, TypeError, ValueError):
        for n in my_list:
            len += 1
        print()
        return (len)
