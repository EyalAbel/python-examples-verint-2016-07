#!/usr/bin/env python

__author__ = 'Eabel'

import sys
import os


class Widget(object):
    

    def __init__(self,name):
        self._name = name
        self._dependencies = set()


    def add_dependency(self,*modules):
        for module in modules:
            self._dependencies.add(module._name)
            self._dependencies.update(module._dependencies)
            

    def build(self):
        print ', '.join(self._dependencies)

########################################################################################################################
#
#
def main():
    luke    = Widget("Luke")
    hansolo = Widget("Han Solo")
    leia    = Widget("Leia")
    yoda    = Widget("Yoda")
    padme   = Widget("Padme Amidala")
    anakin  = Widget("Anakin Skywalker")
    obi     = Widget("Obi-Wan")
    darth   = Widget("Darth Vader")
    _all    = Widget("All")


    luke.add_dependency(hansolo, leia, yoda)
    leia.add_dependency(padme, anakin)
    obi.add_dependency(yoda)
    darth.add_dependency(anakin)

    _all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
    _all.build()
    # code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda,  
    # (can print with newlines in between modules) 
                         
if __name__ == '__main__':
    main()
