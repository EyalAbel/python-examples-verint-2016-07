#!/usr/bin/env python

__author__ = 'Eabel'

import sys
from random import randint

def IsDivisibleBy(n,d):
   return (n%d == 0)

def Exercise2():
    sum = 0
    number_list = list()
    for i in range(7):
        num = randint(1,100);
        sum += num
        number_list.append(num)
    if IsDivisibleBy(sum,7):
        print "Boom"
    print "The sum of the numbers",number_list,"are",`sum`;

########################################################################################################################
#
#
def main():
    Exercise2()

           

if __name__ == '__main__':
    main()