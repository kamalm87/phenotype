if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
    from Num import Num
else:
    from .Num import Num
from Func.Partials import ( 
    Reduction as __func_reduce__,
    Tail      as __func_tail__ )

class Len(Num):
    ''' '''
    __slots__ = ( )
    @classmethod
    def __make__(cls, operation, n):
        ''' '''
        return __func_reduce( len, __func_tail__(operation,n) )
class WithLen(Len):
    ''' '''
    __slots__ = (  )
    @classmethod
    def __make__(cls, operation, n):
        ''' __make__ uses operation, n with the intent to: do something '''
        return __func_head__( filter, super().__make__(operation, n) )
