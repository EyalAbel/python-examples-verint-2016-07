#!/usr/bin/env python

"""
This program concatinate file_1 into file_2

"""
__author__ = 'Eabel'

import sys
import os
import argparse

def is_valid_file_path(file_path):
    if os.path.isfile(file_path):
        return True
    else :      
        print "Error - invalid file path",file_path
        return False

########################################################################################################################
#
#
def main():
    parser = argparse.ArgumentParser(description='This program concatinate file_1 into file_2')
    
    parser.add_argument("file_1", help="path to file")
    parser.add_argument("file_2", help="path to file")    
    args = parser.parse_args()
    if not is_valid_file_path(args.file_1) or not is_valid_file_path(args.file_2):
        sys.exit()

    with open(args.file_1, "r") as src:
        with open(args.file_2, "a") as dst:
            dst.write(src.read())
        
        

    
           

if __name__ == '__main__':
    main()
