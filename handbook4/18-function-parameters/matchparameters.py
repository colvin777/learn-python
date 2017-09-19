'''
Created on 

@author: haoweizh
'''

def tracer(func, name, *pargs, **kargs):
    
    print('calling:', func.__name__)
    return func(*pargs, **kargs)

def func(a, b, c, d = 100):
    return a + b + c + d

print(tracer(func, 1, 2, b =3, c = 4))

def test(a, c, b = 0):pass
'''
def test(a, b = 0, c):pass this have syntaxerror non-default argument follows default argument
because all parameters with default value is follow nod-default
'''
    

    
