_name = 'haoweizh'
_age = 35
__all__ = ['_age']
class Spam:
    numInstances = 0                         # Use static method for class data
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances:", Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)
