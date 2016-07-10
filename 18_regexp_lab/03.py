#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os
import argparse
import re


########################################################################################################################
#
#
def main():
    parser = argparse.ArgumentParser(description='This program receive CVS file with 3 columns and switch the 1st and the 2nd columns')
    
    parser.add_argument("csv_path", help="path to csv file")
    args = parser.parse_args()

    try:
        with open(args.csv_path,'r') as f:
            for line in f:   
                columns = re.split(r',', line)
                if len(columns) != 3:
                    raise Exception("Invalid CSV")
                tmp = columns[0]
                columns[0] = columns[1]
                columns[1] = tmp
                columns[2] = columns[2].rstrip('\n')
                print ','.join(columns)
    except:
        e = sys.exc_info()[0]
        print "Error loading file -",e
                         
if __name__ == '__main__':
    main()
