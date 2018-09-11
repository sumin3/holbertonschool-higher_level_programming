#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end='')
if number > 5:
    print("{:d} and is greater than 5".format(number % 10))
elif number == 0:
    print("{:d} is {:d} and is 0".format(number % 10))
else:
    print("{:d} and is less than 6 and not 0".format(-number % 10))
