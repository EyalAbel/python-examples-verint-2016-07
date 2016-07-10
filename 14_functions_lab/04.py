#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os
import numbers


def longer_than(size,*words):
    """
    Args:
        size (int): size of the min word length
        words (string list): list of words
    Returns:
        int: subset of 'words' list that are longer then 'size'
    """
    if not all(isinstance(item, basestring) for item in words) or not isinstance(size, numbers.Number):
        raise ValueError("Invalid arguments type")
    return [word for word in words if len(word) > size]



