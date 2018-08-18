from functools import ( 
    reduce         as __func_reduce__,
    )
from operator import (
    __ior__,
    __imul__,
    __isub__,
    __iadd__,
    __concat__,
    __itruediv__,
    )
from collections.abc import Callable as __abc_callable__

class _Aggregator(__abc_callable__):
    ''' '''
    def __init__(self, func):
        ''' '''
        self.func = func
    def __call__(self,*items):
        ''' '''
        return __func_reduce__(self.func,items) if items else items
class Aggregator(_Aggregator):
    ''' '''
    def __init__(self, func):
        ''' '''
        super().__init__(func)
IOR    = Aggregator(__ior__)
MUL    = Aggregator(__imul__)
CONCAT = Aggregator(__concat__)
ADD    = Aggregator(__iadd__)
SUB    = Aggregator(__isub__)
DIV    = Aggregator(__itruediv__)
