#!/usr/bin/env python

"""
This program prints the english alphabet (not capital letters) 
"""
__author__ = 'Eabel'

import sys
import os
from itertools import permutations



########################################################################################################################
#
#
def main():
    alphabet = [chr(x) for x in range(ord('a'),ord('z')+1)]
    print alphabet;
      
if __name__ == '__main__':
    main()
