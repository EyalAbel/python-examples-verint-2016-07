#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os
import argparse

def Usage():
    print ('Invalud arguments.\nUsage: 03_bonus.py [path]')


def print_file_by_size(size, root):
    for path, dirs, files in os.walk(root):
        for name in files:
            file_size = os.stat(os.path.join(path, name)).st_size
            if file_size > size:
                print name


########################################################################################################################
#
#
def main():
    path  = "."
    parser = argparse.ArgumentParser(description='ArgumentParser use exercise')
    parser.add_argument("-path", help="path for the working folder")
    args = parser.parse_args()
    if args.path:
        path = args.path
        if not os.path.isdir(path):
            print "Error: path must be a valid (existing) directory" 
    size = 1024 * 1024 # 1 Megabyte
    print_file_by_size(size,path)
    sys.exit()  

           

if __name__ == '__main__':
    main()