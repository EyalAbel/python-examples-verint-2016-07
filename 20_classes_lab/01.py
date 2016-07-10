#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os

class Summer(object):

    def __init__(self):
        self._sum = 0

    def add(self,*nums):
        self._sum += sum(nums)
    
    def total(self):
        return self._sum

########################################################################################################################
#
#
def main():
    s = Summer()
    t = Summer()

    s.add(10, 20)
    t.add(50)
    s.add(30)

    # should print 60
    print s.total()

    # should print 50
    print t.total()    
                         
if __name__ == '__main__':
    main()
