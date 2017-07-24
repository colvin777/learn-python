'''
Created on 

@author: haoweizh
'''
# Manage instances like the prior example, but with a metaclass

def Tracer(classname, supers, classdict):             # On class creation call
    aClass = type(classname, supers, classdict)       # Make client class
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace:', attrname)                 # Catches all but .wrapped 
            return getattr(self.wrapped, attrname)
    print(Wrapper.__dict__)    # Delegate to wrapped object
    return Wrapper

class Person(metaclass=Tracer):                       # Make Person with Tracer
    def __init__(self, name, hours, rate):            # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                              # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate

print(Person.__dict__)
bob = Person('Bob', 40, 50)                           # bob is really a Wrapper
print(bob.name)                                       # Wrapper embeds a Person
print(bob.pay())                                      # Triggers __getattr__

class Person2():                       # Make Person with Tracer
    def __init__(self, name, hours, rate):            # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                              # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate
print(Person2.__dict__)