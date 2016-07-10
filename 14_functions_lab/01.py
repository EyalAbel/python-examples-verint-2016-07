#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os
import numbers



def mysum(*nums):
    """
    Args:
        nums (int list): numbers to accumulate (ignore non integers arguments)
    Returns:
        int: Return an sum of the arguments
    """
    sum = 0
    for num in nums:
        if isinstance(num, numbers.Number):
            sum += num
    return sum

def mymul(*nums):
    """
    Args:
        nums (int list): numbers to multiply (ignore non integers arguments)
    Returns:
        int: Return an multiplaction of the arguments
    """
    mul = 1
    for num in nums:
        if isinstance(num, numbers.Number):
            mul *= int(num)
    return mul

