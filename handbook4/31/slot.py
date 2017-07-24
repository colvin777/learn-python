'''
Created on 

@author: haoweizh
'''
class E:
    __slots__ = ['c', 'd']
    
class D(E):
    __slots__ = ['a', '__dict__']
    

X = D()
X.a = 1; X.b = 2; X.c = 3
print(X.a, X.c)

print(E.__slots__ )                          # But slots are not concatenated
print( D.__slots__)
print( X.__slots__)                           # Instance inherits *lowest* __slots__
print( X.__dict__)                            # And has its own an attr dict

for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
    print(attr, '=>', getattr(X, attr))

print(dir(X))