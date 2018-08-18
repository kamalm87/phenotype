from collections.abc import Callable as __abc_callable__

class Sorter(__abc_callable__):
    ''' '''
    __slots__ = '_key_func', '_reverse'
    def __init__(self, key_func, reverse=False):
        ''' '''
        self._key_func = key_func
        self._reverse  = reverse
    def __call__(self, iterable):
        ''' '''
        return sorted( iterable, key=self._key_func, reverse=self._reverse)
