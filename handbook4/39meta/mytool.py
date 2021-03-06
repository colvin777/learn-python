'''
Created on 

@author: haoweizh
'''
### File: mytools.py
# File mytools.py: assorted decorator tools

def tracer(func):                         # Use function, not class with __call__
    calls = 0                             # Else self is decorator instance only
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

import time
def timer(label='', trace=True):                # On decorator args: retain args
    def onDecorator(func):                      # On @: retain decorated func
        def onCall(*args, **kargs):             # On calls: call original
            start   = time.clock()              # State is scopes + func attr
            result  = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

class test:
    def __init__(self): pass
    def hao(self): pass
    @classmethod
    def test():pass
    @staticmethod
    def testtwo():pass
        