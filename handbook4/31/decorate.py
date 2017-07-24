'''
Created on 

@author: haoweizh
'''
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func  = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s'  % (self.calls, self.func.__name__))
        self.func(*args)

@tracer                       # Same as spam = tracer(spam)
def spam(a, b, c):            # Wrap spam in a decorator object
    print(a, b, c)
# spam = tracer(spam)

spam(1, 2, 3)                 # Really calls the tracer wrapper object
spam('a', 'b', 'c')           # Invokes __call__ in class
spam(4, 5, 6)                 # __call__ adds logic and runs original object
print('-' * 20)
def generate():                  # Fails prior to Python 2.2, works later
    class Spam:
        count = 1
        def method(self):        # Name Spam not visible:
            print(Spam.count)    # not local (def), global (module), built-in
    return Spam()

generate().method()

class Spam:                                                              
    count = 1                                                            
    def method(self):        # Name Spam not visible:                    
        print(Spam.count)    # not local (def), global (module), built-in
Spam().method()

def one():
    a = 'hao'
    def two():
        print(a)
    two()
one()