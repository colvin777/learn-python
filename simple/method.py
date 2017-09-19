class Methods:
    va = 9
    def imeth(self, x):            # Normal instance method: passed a self
        print(self, x)

    def smeth(x):  
        va = x                # Static: no instance passed
        print(va)

    def cmeth(cls, x):             # Class: gets class, not instance
        print(cls, x)

    smeth = staticmethod(smeth)    # Make smeth a static method
    cmeth = classmethod(cmeth)     # Make cmeth a class method
