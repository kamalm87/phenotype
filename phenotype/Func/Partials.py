from functools import ( 
    partial        as __ft_partial__,
    update_wrapper as __ft_update_wrapper__,
    reduce         as __ft_reduce__,
    )
from collections.abc import Callable as __abc_callable__
#1 PARTIALS
#2 BASE CLASS
class _Partial(__abc_callable__):
    ''' '''
    __slots__ = 'func', 'args', 'keywords'
    def __init__(self, func, *args, **kwargs):
        ''' '''
        self.func     = func
        self.args     = args
        self.keywords = kwargs
    @classmethod
    def __head__(cls, function, *args, **kwargs):
        ''' '''
        return __ft_update_wrapper__( __ft_partial__(function, *args, **kwargs), function )
    @classmethod
    def __tail__(cls, function, *w_args, **kwargs):
        ''' '''
        def _rpartial(*args, **kwargs):
            new_kwargs = kwargs.copy()
            new_kwargs.update(kwargs)
            return function( *args, *w_args, **new_kwargs)
        return __ft_update_wrapper__( _rpartial, function )
    def __call__(self, *args, **kwargs):
        ''' '''
        return self.func(*args, **kwargs)
#2 PUBLIC CLASSES
class Head(_Partial):
    ''' '''
    def __init__(self, function, *args, **kwargs):
        ''' '''
        super().__init__(self.__head__(function, *args, **kwargs), *args, **kwargs)
class Tail(_Partial):
    ''' '''
    def __init__(self, function, *args, **kwargs):
        ''' '''
        super().__init__(self.__tail__(function, *args, **kwargs), *args, **kwargs)
#1 REDUCTIONS
class Reduction(list):
    ''' '''
    def __init__(self, *function_sequence):
        ''' '''
        super().__init__(function_sequence)
    def __call__(self, initial):
        ''' '''
        return self.__reduction__( self, initial )
    @staticmethod
    def __step__(item, reducer):
        ''' '''
        return reducer(item)
    @classmethod
    def __reduction__(cls, sequence, item=None):
        ''' '''
        def _reduce(*args): return __ft_reduce__(cls.__step__, *args)
        return _reduce(sequence, item)
    @classmethod
    def Reduce(cls, item, *function_sequence):
        ''' '''
        return cls.__reduction__( function_sequence, item )
