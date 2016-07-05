#!/usr/bin/env python

__author__ = 'Eabel'

import sys

def Exercise4():
    input_list = list();
    print "Please enter your input:" 
    while True:
        row = raw_input();
        if not row:
            break
        input_list.insert(0,row);
    print "You entered (in reverse):" 
    print '\n'.join(input_list)

########################################################################################################################
#
#
def main():
    Exercise4()

           

if __name__ == '__main__':
    main()