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
    parser = argparse.ArgumentParser(description='This program receive config file path and varible name and prints the varible value')
    
    parser.add_argument("config_path", help="path to config file")
    parser.add_argument("varible_name", help="varible name")
    args = parser.parse_args()

    try:
        regex_str = '\s*' + args.varible_name + '\s*=\s*(.*)'
        with open(args.config_path,'r') as f:
            for line in f:   
                res = re.search(regex_str, line)
                if res is not None:
                    print  args.varible_name,'value is',res.group(1)
                    return
        print 'No match for',args.varible_name
    except:
        e = sys.exc_info()[0]
        print "Error loading file -",e
                         
if __name__ == '__main__':
    main()
