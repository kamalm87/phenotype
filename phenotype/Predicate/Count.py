if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
    from Base import (
        Invert, 
        Never,
        __func_apply__,
        __func_reduce__,
        __func_head__,
        __func_tail__,
        )
else:
    from .Base import (
        Invert, 
        Never,
        __func_apply__,
        __func_reduce__,
        __func_head__,
        __func_tail__,
        )
from operator    import ( 
    attrgetter as __op_attr_getter__,
    lt       as __lt__,
    le       as __le__,
    eq       as __eq__,
    ne       as __ne__,
    ge       as __ge__,
    gt       as __gt__,
    not_     as __not__,
    contains as __contains__, )

class Count(object):
    ''' '''
    __slots__ = ( )
    @classmethod
    def _Count(cls, *predicates):
        ''' '''
        return __func_reduce__( __func_apply__(*predicates), sum )
    @classmethod
    def Match(cls, n, comparison, *predicates):
        ''' '''
        return __func_reduce__( cls._Count(*predicate), __func_tail__(comparison,n) )
    @classmethod
    def Is(cls, *predicates, n=1):
        ''' '''
        return cls.Match( n, __eq__, *predicates)
    @classmethod
    def Not(cls, *predicates, n=1):
        ''' '''
        return cls.Match( n, __ne__, *predicates)
    @classmethod
    def Less(cls, *predicates, n=1):
        ''' '''
        return cls.Match( n, __lt__, *predicates)
    @classmethod
    def Least(cls, *predicates, n=1):
        ''' '''
        return cls.Match( n, __le__, *predicates)
    @classmethod
    def Most(cls, *predicates, n=1):
        ''' '''
        return cls.Match( n, __ge__, *predicates)
    @classmethod
    def More(cls, *predicates, n=1):
        ''' '''
        return cls.Match( n, __gt__, *predicates)
