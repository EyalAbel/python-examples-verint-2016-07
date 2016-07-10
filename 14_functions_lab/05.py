#!/usr/bin/env python


__author__ = 'Eabel'

import sys
import os
from collections import defaultdict


def groupby(key_func,*values):
    """
    Returns:
    
        dictionary:  grouped by value of key_func(v) (for v in values)
    """
    d = defaultdict(list)
    for value in values:
        d[key_func(value)].append(value)
    return d
