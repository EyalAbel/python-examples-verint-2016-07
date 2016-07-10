#!/usr/bin/env python
"""
This program writh lines from fine_1 and file_2 alternately into file_2
"""
__author__ = 'Eabel'

import sys
import os
import argparse
import itertools

def create_dictionaries(file_path):
    dir = os.path.dirname(file_path)
    if not os.path.exists(dir):
        os.makedirs(os.path.dirname(file_path))

def load_file(file_path):
    with open(file_path,'r') as f:
        for line in f:
            yield line
########################################################################################################################
#
#
def main():
    parser = argparse.ArgumentParser(description='This program writh lines from fine_1 and file_2 alternately into file_2')
    
    parser.add_argument("file_1", help="path to file")
    parser.add_argument("file_2", help="path to file")
    parser.add_argument("file_3", help="path to file")
    args = parser.parse_args()

    if os.path.isfile(args.file_3):
        print "Error - file",args.file_3,"alrady exist"
        sys.exit()

    try:
        create_dictionaries(args.file_3)

        file1_lines = load_file(args.file_1)
        file2_lines = load_file(args.file_2)
        with open(args.file_3, "w") as dst:
            itr = itertools.izip_longest(file1_lines, file2_lines)
            for item in itr:
              if item[0]:            
                dst.write(item[0])
              if item[1]:  
                dst.write(item[1])     
              #file3_lines = filter(None, sum(itertools.izip_longest(file1_lines, file2_lines), ()))

    except:
        e = sys.exc_info()[0]
        print "Error -",e
                         
if __name__ == '__main__':
    main()
