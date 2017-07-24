'''
Created on 

@author: haoweizh
'''

import sys

from chapter27.tt import classtools


print(sys.path)
# from tt import classtools
print(classtools.AttrDisplay())
def get_include(): 
    print(__path__[0])