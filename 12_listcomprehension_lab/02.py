#!/usr/bin/env python

"""
This program prints the english alphabet non capital letters permutations of length 3 with repeats 
"""
__author__ = 'Eabel'

import sys
import os
import itertools


########################################################################################################################
#
#
def main():
    alphabet = [chr(x) for x in range(ord('a'),ord('z')+1)]
    print '\n'.join([''.join(p) for p in itertools.product(alphabet, repeat=3)])
      
if __name__ == '__main__':
    main()
