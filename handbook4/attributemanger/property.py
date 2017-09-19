'''
Created on 

@author: haoweizh
'''

class Person:
    
    def __init__(self, sal):
        self.sal = sal
    @property
    def name(self):
        "name property docs"
        print('fetch ...')
        
    @name.setter
    def name(self, value):
        "name property docs"
        print('set ...')
    @name.deleter
    def name(self):
        print('delete ....')
        
    #name = property(name, sname, tname)
p = Person('high')
print(p.name)
del p.name
p.name = 'hao'

class Hello:
    __slots__ =['name','age','__dict__']
    def __getattr__(self, attr):
        if(attr == 'age'):
            return 50
    def __setattr__(self, attr, value):
        if(attr not in list(self.__dict__) +  self.__slots__):
            self.__dict__[attr] = value
        else:
            self.attr = value

h = Hello()
print(h.age)
h.name = 'ha'
print(h.name)