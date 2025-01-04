from abc import ABC, abstractmethod

class par(ABC):
    @abstractmethod
    def f(self):
        pass

class child(par):
    # not implementing f() will result in error
    pass
    '''def f(self):
        pass'''

c = child()
c.f()