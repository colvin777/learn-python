'''
Created on 

@author: haoweizh
'''
import sys
print(sys.path)
class per:
    x = 'hao'
    def change(self, value):
        per.x = value
    
    
a = per();
print(a.x)
print(per.__dict__)
a.change('wei')
print(a.x)
print(a.__dict__)
print('*'* 30)
from chapter23_module_package import importrelativeaAndabsolute