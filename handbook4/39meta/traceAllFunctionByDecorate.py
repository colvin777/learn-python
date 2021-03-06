'''
Created on 

@author: haoweizh
'''
import mytool
from mytool import tracer

print(mytool.__dict__)
print('_' * 20)
print(mytool.test().__dict__)
class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @tracer
    def giveRaise(self, percent):         # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)       # onCall remembers giveRaise

    @tracer
    def lastName(self):                   # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                        # Runs onCall(sue, .10)
print(sue.pay)
print(bob.lastName(), sue.lastName())     # Runs onCall(bob), remembers lastName