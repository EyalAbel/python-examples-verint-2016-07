#!/usr/bin/env python

__author__ = 'Eabel'

import sys

def Exercise1():
    print "Please enter 10 numbers:"
    max_val = -sys.maxint - 1 # Min int value
    for i in range(10):
        try:
            max_val = max(int(raw_input()),max_val)
        except ValueError:
            print "Please enter only numbers"
            sys.exit()  

    print "The biggest number is:", max_val

########################################################################################################################
#
#
def main():
    Exercise1()

           

if __name__ == '__main__':
    main()