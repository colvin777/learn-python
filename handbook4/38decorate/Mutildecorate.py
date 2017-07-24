'''
Created on 

@author: haoweizh
'''
def d1(F): return lambda x : 'X' + F(x)
def d2(F): return lambda x : 'Y' + F(x)
def d3(F): return lambda x : 'Z' + F(x)

@d1
@d2
@d3
def func(x):
    return x + 'spam'

print(func('ha'))


        