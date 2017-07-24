'''
Created on 

@author: haoweizh
'''
def decorate(A, B):
    print(A, B)
    def actualDecorate(F):
        return F
    return actualDecorate

@decorate(A='wei', B='wei')
def fun(x, y):
    print(x,y)

fun('a', 'b')