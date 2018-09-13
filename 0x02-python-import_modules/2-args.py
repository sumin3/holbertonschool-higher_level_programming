#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = ':'
    if (len(sys.argv) == 1):
        c = '.'
    print("{:d} arguments{:s}".format(len(sys.argv) - 1, c))
    for i in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(i, sys.argv[i]))
