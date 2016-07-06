#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os


def Usage():
    print ('Invalud arguments.\nUsage: 03.py [path]')


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
    if len(sys.argv) > 2:
        Usage()
        sys.exit()
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if not os.path.isdir(path):
            print Usage()   
    size = 1024 * 1024 # 1 Megabyte
    print_file_by_size(size,path)

           

if __name__ == '__main__':
    main()