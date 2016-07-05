#!/usr/bin/env python

__author__ = 'Eabel'

import sys
from random import randint

def digits_sum(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def Exercise3():
    rand_num = randint(1,10000);
    dig_sum = digits_sum(rand_num)
    print "The sum of",rand_num,"digits is", dig_sum

########################################################################################################################
#
#
def main():
    Exercise3()

           

if __name__ == '__main__':
    main()