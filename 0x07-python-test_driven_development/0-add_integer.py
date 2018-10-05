#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def add_integer(a, b=98):
    """ This is a function that add two integers
    Args:
       a: first integer that need to add
        b: second integer that need to add
    Return:
        return: sum
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b
