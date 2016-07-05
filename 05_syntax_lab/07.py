#!/usr/bin/env python

__author__ = 'Eabel'

import sys
from random import randint

def IsDivisibleBy(n,d):
   return (n%d == 0)

def compare(x,y):
    if x == y:
        return 0
    elif x < y:
        return 1
    else:
        return -1

def compareWithPossibleMistake(x,y):
    num = randint(1,100);
    comp = compare(x,y);
    if not IsDivisibleBy(num,7):
        return comp
    else:    
        if comp == -1:
            return 1;
        elif comp == 1:
            return -1
        else:
            return comp


def Exercise7():
    num = randint(1,100);
    ansMap = {1: "Too big, try again.", -1:"Too small, try again.", 0:"You got a match."}
    
    print "Please guess a number between 1 to 100:"

    while True:
        try:
            compRes = compareWithPossibleMistake(num,int(raw_input()))
            print ansMap[compRes]
            if not compRes:
                break
        except ValueError:
            print "Please enter only numbers"
            sys.exit()  

########################################################################################################################
#
#
def main():
    Exercise7()

           

if __name__ == '__main__':
    main()