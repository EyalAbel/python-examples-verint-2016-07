#!/usr/bin/env python

__author__ = 'Eabel'

import sys


def Usage():
    print ('Invalud arguments.\nUsage: 02.py N1 N2')
########################################################################################################################
#
#
def main():
    if len(sys.argv) != 3:
        Usage()
        sys.exit()
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print num1,'+',num2,'=',num1+num2
    except ValueError:
        Usage()
        sys.exit()  
           

if __name__ == '__main__':
    main()