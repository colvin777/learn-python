'''
Created on 

@author: haoweizh
'''

def kwonly(a, *b, c):
    print(a, b,c)
    
kwonly(1, 2, 3, c =1)

def k(a, *, b, c):
    print(a, b, c)
k(1,  b = 1, c = 3)

def s(a, *, b = 1, c = 3):
    print(a, b, c)
s(1)
# def kw(a, **args, c):pass

def kw(a, *b, c, **d): pass

def f(a, *b, c=6, **d):print(a,b ,c,d)
f(1, *(2, 3), **dict(x=4, y=5))
f(1, 2, 3, x=4, y=5)

def fs(a, b, c = 1):print(a, b, c)
fs(1, 2)