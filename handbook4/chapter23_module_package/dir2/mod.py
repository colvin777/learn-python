'''
Created on 

@author: haoweizh
'''

# show different result use python2.7 and python3.5
# in python2.7 (import  string  default search this package then go to sys.path)
#     in mod.py
#     <type 'module'>
#     D:\Code\python\learn_python_handbook4\chapter23_module_package\dir2\string.py
#     <type 'module'>
#     D:\Code\python\learn_python_handbook4\chapter23_module_package\dir2\string.py
# in python3.5  (import  string  default search in sys.path)
#     in mod.py
#     <class 'module'>
#     D:\Code\python\learn_python_handbook4\chapter23_module_package\dir2\string.py
#     <class 'module'>
#     C:\Program Files\Python 3.5\lib\string.py

#import string
import sys
print(sys.path)


print('in mod.py')
z = 3

from . import  string
 
print(type(string))
print(string.__file__)

import  string

print(type(string))
print(string.__file__)