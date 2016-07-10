#!/usr/bin/env python


__author__ = 'Eabel'

import sys
import os



def sum_second_digits(*nums):
    """
    Args:
        nums (int list): list of numbers
    Returns:
        int: sum the second digit of each number
    """
    try:
        return sum( [ (number / 10) % 10 for number in nums ] )
    except:
        e = sys.exc_info()[0]
        raise ValueError(e)


########################################################################################################################
#
#
def main():
    sum_second_digits(445,325,111)
    sum_second_digits(445,'443',111)
 


      
if __name__ == '__main__':
    main()
