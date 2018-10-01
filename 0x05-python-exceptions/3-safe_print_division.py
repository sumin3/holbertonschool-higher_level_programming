#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:0.1f}".format(result))
        return result
    except (ZeroDivisionError, ValueError):
        print("Inside result: None")
        return None
