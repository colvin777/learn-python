'''
Created on 

@author: haoweizh
'''
'''
Created on 

@author: haoweizh
'''
class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self._acct = acct                         # Instance data
        self._name = name                         # These trigger __set__ calls too
        self._age  = age                          # __X not needed: in descriptor
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    class Name:
        def __get__(self, instance, owner):      # Class names: CardHolder locals
            return instance._name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            instance._name = value
    name = Name()
        
    class Age:
        def __get__(self, instance, owner):
            return instance._age                             # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                instance._age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            #return instance._acct
            return instance._acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:          # Use instance class data
                raise TypeError('invald acct number')
            else:
                instance._acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age    # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')        # Else set allowed here
    remain = Remain()


print(CardHolder.__dict__)
'''{

 
'age': <__main__.CardHolder.Age object at 0x00000000029E4630>,
 'name': <__main__.CardHolder.Name object at 0x00000000029E45F8>,
 'remain': <__main__.CardHolder.Remain object at 0x00000000029E46A0>, 
 'acct': <__main__.CardHolder.Acct object at 0x00000000029E4668>, 
 
  '__dict__': <attribute '__dict__' of 'CardHolder' objects>, 
  '__weakref__': <attribute '__weakref__' of 'CardHolder' objects>, 
  '__doc__': None, 
  '__module__': '__main__', 
  '__init__': <function CardHolder.__init__ at 0x0000000002972AE8>, 

  'Age': <class '__main__.CardHolder.Age'>, 
  'Name': <class '__main__.CardHolder.Name'>
  'Remain': <class '__main__.CardHolder.Remain'>,
  'Acct': <class '__main__.CardHolder.Acct'>, 
  
'retireage': 59.5,
'acctlen': 8, 

}
'''
 

card = CardHolder('yes11111', 'colvin', 33, 'shanghai')
print(card.__dict__)
#{'_acct': 'yes11111', '_name': 'colvin', '_age': 33, 'addr': 'shanghai'}

print(card.acct)
print(card.addr)
print(card.remain)
card2 = CardHolder('hhhhhhhh', 'colvin', 33, 'shanghai')
print(card.acct)
print(card2.acct)

