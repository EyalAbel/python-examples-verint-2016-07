#!/usr/bin/env python

"""
This program get words list in a file and prints all of the anagrams

"""
__author__ = 'Eabel'

import sys
import os
import argparse
from collections import defaultdict


def load_words_file(file_path):
    try:
        with open(file_path) as f:
            for word in f:
                yield word.rstrip()
    except:
        e = sys.exc_info()[0]
        print "Error loading file -",e

def get_anagrams(words):
    d = defaultdict(list)
    for word in words:
        key = sorted(word)
        d[tuple(key)].append(word)
    return d

def print_anagrams(anagrams):
    if len(anagrams) == 1:
        print anagrams[0]
    else:
        for i in range(len(anagrams)-1):
            for j in range(1,len(anagrams)):
                print anagrams[i],anagrams[j]
            

def print_all_anagrams(words):
    d = get_anagrams(words)
    for key, anagrams in d.iteritems():
        if len(anagrams) > 0:
            print_anagrams(anagrams)



########################################################################################################################
#
#
def main():
    parser = argparse.ArgumentParser(description='This program get words list in a file and prints all of the anagrams')
    
    parser.add_argument("file_path", help="path to the word list file")
    args = parser.parse_args()   

    words = load_words_file(args.file_path)

    print_all_anagrams(words)
    sys.exit()

        
if __name__ == '__main__':
    main()
