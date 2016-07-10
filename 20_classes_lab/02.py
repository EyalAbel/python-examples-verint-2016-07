#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os

class MyCounter(object):
    count = 0

    def __init__(self):
        MyCounter.count += 1


########################################################################################################################
#
#
def main():
    for _ in range(10):
         c1 = MyCounter()

    # should print 10
    print MyCounter.count 
                         
if __name__ == '__main__':
    main()
