#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os
import numbers


def foo(str_arg, num_arg):
    """
    Args:
        str_arg (string): string arg
        num_arg (string): number arg
    Returns:
        int: prints the args
    """
    if not isinstance(num_arg, numbers.Number) or not isinstance(str_arg, basestring):
        raise ValueError("Invalid arguments type")
    print str_arg,num_arg



