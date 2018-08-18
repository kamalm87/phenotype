from operator import ( 
    attrgetter as __op_attr_getter__,
    itemgetter as __op_item_getter__,)
from .Auxiliary import (
    ReturnAs  as __return_as__,
    TryExcept as __try_except__,)
#2 LOCAL GLOBALS
__try__ = __try_except__.Unary
#2 PUBLIC INTERFACE
def Item(index): return __op_item_getter__(index)
def Sliced(*indices): return __op_attr_getter__(tuple(indices))
def Name(name,default=None): return __try__(__op_attr_getter__(name), __return_as__(default) )
