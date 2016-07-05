#!/usr/bin/env python

__author__ = 'Eabel'

import sys
from random import randint

# define gcd function
def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# define lcm function
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

def Exercise6():
    num1 = randint(1,10);
    num2 = randint(1,10);
    print "The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2)

########################################################################################################################
#
#
def main():
    Exercise6()

           

if __name__ == '__main__':
    main()