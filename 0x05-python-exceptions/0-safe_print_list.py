#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    s = ""
    s1 = ""
    len = 0
    try:
        for i in range(0, x):
            s += str(my_list[i])
        num = int(s)
        print(s)
        return (i + 1)
    except (IndexError, TypeError, ValueError):
        for n in my_list:
            s1 += str(n)
            len += 1
        num = int(s1)
        print(num)
        return (len)
