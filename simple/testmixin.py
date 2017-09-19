from lister import *                  # Get lister tool classes

class Super:
    def __init__(self):               # Superclass __init__
        self.data1 = 'spam'           # Create instance attrs
    def ham(self):
        pass
class Sub(Super, ListTree): 
    pass

print(7152108694%3599)

if __name__ == '__main__':
    X = Sub()
    print(X)                          # Run mixed-in __str__
