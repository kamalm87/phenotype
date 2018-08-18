if __name__ == '__main__':
    from sys     import path    as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from Func.Partials import ( 
        Head      as __func_head__,
        Reduction as __func_reduce__,
        )
from Core.Get      import Name as __get_name__

class Filter(object):
    ''' '''
    __slots__   = ( )
    __default__ = __func_head__( filter, None )
    @classmethod
    def ByAttribute(cls, name):
        ''' ByAttribute uses name with the intent to: '''
        return __func_head__( filter, __get_name__(name) )
    @classmethod
    def WithAttribute(cls, name):
        ''' WithAttribute uses name with the intent to: do something '''
        return __func_reduce__(cls.ByAttribute(name), cls.__default__)
