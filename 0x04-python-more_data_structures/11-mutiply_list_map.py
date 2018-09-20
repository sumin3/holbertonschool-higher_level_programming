#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    new = my_list.copy()
    new = list(map(lambda i: i * number, new))
    return new
