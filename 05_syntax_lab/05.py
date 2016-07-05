#!/usr/bin/env python

__author__ = 'Eabel'

import sys
from random import randint

def IsDivisibleBy(n,d):
   return (n%d == 0)

def Exercise5():
    while True:
        rand_num = randint(1,1000000);       
        if IsDivisibleBy(rand_num,15) and IsDivisibleBy(rand_num,13) and IsDivisibleBy(rand_num,7):
            print rand_num,"Divisible by 7, 13 and 15"
            break;

########################################################################################################################
#
#
def main():
    Exercise5()

           

if __name__ == '__main__':
    main()