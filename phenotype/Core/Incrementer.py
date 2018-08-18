from functools import ( partial as __ft_partial__)
from operator  import ( __iadd__, __lt__ )

class Incrementer(object):
    ''' '''
    __slots__ = 'i', 'n', 'by'
    def __init__(self, n, i=0, by=1):
        ''' '''
        self.n = n
        self.i = i
        self.by = __ft_partial__(__iadd__,by)
    def __increment__(self):
        ''' '''
        self.n = self.by(self.n)
    @property
    def __continue__(self):
        ''' '''
        return self.i < self.n
    def __bool__(self):
        ''' '''
        if self.__continue__:
            self.__increment__()
            return True
        return False
    def __iadd__(self, inc):
        ''' '''
        self.i = i
        return self
    def __lt__(self, val):
        ''' '''
        return self.i < val
    def __eq__(self, val):
        ''' '''
        return self.i == val
    def __gt__(self, val):
        ''' '''
        return self.i > val
    def __call__(self, *args, **kwargs):
        ''' '''
        return bool(self)
