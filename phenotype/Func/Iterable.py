if __name__ == '__main__':
    from sys       import path    as __sys_path__
    from os.path   import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from itertools import (
    starmap     as __it_starmap__,
    filterfalse as __it_filter_false__,
    dropwhile   as __it_drop_while__,
    takewhile   as __it_take_while__,
    )
from functools import ( 
    partial         as __ft_partial__,
    update_wrapper  as __ft_update_wrapper__,
    )
from Func.Partials import Head as __func_head__, Tail as __func_tail__

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
