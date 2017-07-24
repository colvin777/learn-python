
"this is only test!"



from abc import ABCMeta, abstractmethod
from test.pickletester import metaclass

class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplemented('action must be defined!')
class Sub(Super): pass


class Asuper(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass
class Asub(Asuper):
    def action(self):
        print('in Asub')