from phenotype.Func import (
    __it_starmap__,
    __it_filter_false__,
    __it_drop_while__,
    __it_take_while__,
    )
from phenotype.Func.Partials import Head as __func_head__, Tail as __func_tail__

class _Iterable:
    ''' '''
    @staticmethod
    def __binary__(x,y):
        return x,y
    __tail__ = __func_tail__
    __head__ = __func_head__
    @classmethod
    def Function(cls, function):
        ''' '''
        return cls.__func_head__(cls.__binary__,function)
    @classmethod
    def Iterable(cls, iterable):
        ''' '''
        return cls.__func_tail__(cls.__binary__,iterable)
class Map(_Iterable):
    ''' '''
    __binary__ = staticmethod(map)
class StarMap(_Iterable):
    ''' '''
    __binary_iterable_function__ = __it_starmap__
class Filter(_Iterable):
    ''' '''
    __binary__ = staticmethod(filter)
class FilterFalse(_Iterable):
    ''' '''
    __binary__ = staticmethod(__it_filter_false__)
class DropWhile(_Iterable):
    ''' '''
    __binary__ = staticmethod(__it_drop_while__)
class TakeWhile(_Iterable):
    ''' '''
    __binary__ = staticmethod(__it_take_while__)
