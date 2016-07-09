#!/usr/bin/env python
"""
This program writh lines from fine_1 and file_2 alternately into file_2
"""
__author__ = 'Eabel'

import sys
import os
import argparse
import itertools

def is_valid_file_path(file_path):
    if os.path.isfile(file_path):
        return True
    else :      
        print "Error - invalid file path",file_path
        return False

def create_dictionaries(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc: 
            if exc.errno != errno.EEXIST:           
                return False
    return True

########################################################################################################################
#
#
def main():
    path  = "."
    parser = argparse.ArgumentParser(description='This program writh lines from fine_1 and file_2 alternately into file_2')
    
    parser.add_argument("file_1", help="path to file")
    parser.add_argument("file_2", help="path to file")
    parser.add_argument("file_3", help="path to file")
    args = parser.parse_args()
    if not is_valid_file_path(args.file_1) or not is_valid_file_path(args.file_2):
        sys.exit()
    if os.path.isfile(args.file_3):
        print "Error - file",args.file_3,"alrady exist"
        sys.exit()
    if not create_dictionaries(args.file_3):
        print "Error - failed to create file dictionaries"
        sys.exit()
    

    with open(args.file_1, "r") as src1:
        with open(args.file_2, "r") as src2:
            with open(args.file_3, "w") as dst:        
                file1_lines = src1.readlines()
                file2_lines = src2.readlines()
                file3_lines = filter(None, sum(itertools.izip_longest(file1_lines, file2_lines), ()))
                dst.writelines(file3_lines)
                
        
        

    
           

if __name__ == '__main__':
    main()
