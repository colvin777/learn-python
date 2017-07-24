# encoding: utf-8
'''
Created on 2017年6月6日

@author: haoweizh
'''

def test(*arg):
    print(type(arg))
    return arg

def t(t, s, y):
   print(t,s,y)
t(* test(1, 2, 3))
