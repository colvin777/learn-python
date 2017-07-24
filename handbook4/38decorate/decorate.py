'''
Created on 

@author: haoweizh
'''
from _ast import Nonlocal
def decorator(cls):
    class Wrapper:
        def __init__(self, *args):
            print('in wrapper')
            self.wrapped =  cls(*args)
        def __getattr__(self, name):
            print('__getattr__')
            return getattr(self.wrapped, name)
    return Wrapper

#@decorator
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

b =decorator(C)
y=b(1,3)
y.x

class X:
    def __getattr__(self, name):
            print('__getattr__')
x = X()
x.g



def count(f):
    count = 0
    def wf(*args):
        nonlocal count
        count +=1
        print(count)
        f(*args)
    return wf
@count
def client():pass
client()
client()
client()
client()


