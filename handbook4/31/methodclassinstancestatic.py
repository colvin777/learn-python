'''
Created on 

@author: 
'''
class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print(self, x)

    def smeth(x):                  # Static: no instance passed
        print(x)

    def cmeth(cls, x):             # Class: gets class, not instance
        print(cls, x)

    smeth = staticmethod(smeth)    # Make smeth a static method
    cmeth = classmethod(cmeth)     # Make cmeth a class method

obj = Methods()                # Make an instance                      
                                                                       
obj.imeth(1)                   # Normal method, call through instance                                                                      
Methods.imeth(obj, 2)          # Normal method, call through class     
                                                                       
Methods.smeth(3)               # Static method, call through class                                                                          
obj.smeth(4)                   # Static method, call through instance  


Methods.cmeth(5)               # Class method, call through class                                                                          
obj.cmeth(6)                   # Class method, call through instance   
