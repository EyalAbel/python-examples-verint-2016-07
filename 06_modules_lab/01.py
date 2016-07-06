#!/usr/bin/env python

__author__ = 'Eabel'

import sys


def Usage():
    print ('Invalud arguments.\nUsage: 01.py N')
########################################################################################################################
#
#
def main():
    if len(sys.argv) != 2:
        Usage()
        sys.exit()
    try:
        for i in range(int(sys.argv[1])):
            print 'Hello Python'
    except ValueError:
        Usage()
        sys.exit()  
           

if __name__ == '__main__':
    main()