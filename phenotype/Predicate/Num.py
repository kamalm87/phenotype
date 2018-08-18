if __name__ == '__main__':
    from sys     import ( path    as __sys_path__ )
    from os.path import ( abspath as __abs_path__ )
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
    lt       as __lt__,
    le       as __le__,
    eq       as __eq__,
    ne       as __ne__,
    ge       as __ge__,
    gt       as __gt__,
    )

class Num(object):
    ''' '''
    __slots__ = ( )
    @classmethod
    def __make__(cls, operation, n):
        ''' '''
        return __func_tail__(operation,n)
    @classmethod
    def __compound__(cls, numbers, predicates ):
        ''' '''
        def __coalesce__(): yield from ( fn(num) for num, fn in zip(numbers,predicates))
        return __func_reduce__( __func_apply__(*__coalesce__()), all ) 
    @classmethod
    def Equal(cls, n):
        ''' '''
        return cls.__make__(__eq__,n)
    @classmethod
    def Not(cls, n):
        ''' '''
        return cls.__make__(__ne__,n)
    @classmethod
    def Less(cls, n):
        ''' '''
        return cls.__make__(__lt__,n)
    @classmethod
    def More(cls, n):
        ''' '''
        return cls.__make__(__gt__,n)
    @classmethod
    def Most(cls, n):
        ''' '''
        return cls.__make__(__le__,n)
    @classmethod
    def Least(cls, n):
        ''' '''
        return cls.__make__(__ge__,n)
    @classmethod
    def Within(cls, i, j):
        ''' '''
        return cls.__compound__( (i,j), (cls.Least, cls.Most) )
    @classmethod
    def Inside(cls, i, j):
        ''' '''
        return cls.__compound__( (i,j), (cls.More, cls.Less) )
    @classmethod
    def FromUntil(cls, i, j):
        ''' '''
        return cls.__compound__( (i,j), (cls.Least, cls.Less) )
    @classmethod
    def AfterUpTo(cls, i, j):
        ''' '''
        return cls.__compound__( (i,j), (cls.More, cls.Most) )
class WithNum(Num):
    ''' '''
    __slots__ = (  )
    @classmethod
    def __make__(cls, operation, n):
        ''' __make__ uses operation, n with the intent to: do something '''
        return __func_head__( filter, super().__make__(operation, n) )
