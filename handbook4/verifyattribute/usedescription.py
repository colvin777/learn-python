'''
Created on 

@author: haoweizh
'''
class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __set__ calls too
        self.age  = age                          # __X not needed: in descriptor
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    class Name:
        def __get__(self, instance, owner):      # Class names: CardHolder locals
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()
        
    class Age:
        def __get__(self, instance, owner):
            return self.age                             # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            #return instance._acct
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:          # Use instance class data
                raise TypeError('invald acct number')
            else:
                self.acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age    # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')        # Else set allowed here
    remain = Remain()


print(CardHolder.__dict__)
'''{
'acctlen': 8, 
 retireage': 59.5, 
 
'__doc__': None,
 '__dict__': <attribute '__dict__' of 'CardHolder' objects>, 
 '__init__': <function CardHolder.__init__ at 0x0000000002982AE8>,
 '__weakref__': <attribute '__weakref__' of 'CardHolder' objects>,
  '__module__': '__main__'
  
 'acct': <__main__.CardHolder.Acct object at 0x00000000029F46A0>,  
 'age': <__main__.CardHolder.Age object at 0x00000000029F4668>, 
 'name': <__main__.CardHolder.Name object at 0x00000000029F4630>, '
 'remain': <__main__.CardHolder.Remain object at 0x00000000029F46D8>, 
 
 'Age': <class '__main__.CardHolder.Age'>, 
 'Acct': <class '__main__.CardHolder.Acct'>, 
 'Remain': <class '__main__.CardHolder.Remain'>, 
 'Name': <class '__main__.CardHolder.Name'>, 
}'''
 

card = CardHolder('yes11111', 'colvin', 33, 'shanghai')
print(card.__dict__)
#{'addr': 'shanghai'}

print(card.acct)
print(card.addr)
print(card.remain)
card2 = CardHolder('hhhhhhhh', 'colvin', 33, 'shanghai')
print(card.acct)
