#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os
import argparse
import re


def to_camel_case(s):
    """
    Converting Snake Case to Lower Camel Case
    Args:
        s (String): Snake Case string
    Returns:
        String: Lower Camel Case string
    """
    return re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), s)

def to_snake_case(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
