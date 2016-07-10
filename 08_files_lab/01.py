#!/usr/bin/env python

"""
This program concatinate file_1 into file_2

"""
__author__ = 'Eabel'

import sys
import os
import argparse



########################################################################################################################
#
#
def main():
    parser = argparse.ArgumentParser(description='This program concatinate file_1 into file_2')
    
    parser.add_argument("file_1", help="path to file")
    parser.add_argument("file_2", help="path to file")    
    args = parser.parse_args()

    try:     
        with open(args.file_1, "r") as src:
            with open(args.file_2, "a") as dst:
                for line in src:
                    dst.write(line)
    except:
        e = sys.exc_info()[0]
        print "Error -",e
        
        

    
           

if __name__ == '__main__':
    main()
