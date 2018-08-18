if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from operator      import __contains__
from enum          import ( auto as __enum_auto__, Flag as __enum_flag__ )
from Core.Get      import ( Name as __get_name__ )
from Func.Partials import (
    Head       as __func_head__,
    Reduction as __func_reduce__,
    )
from Func.Aggregator import ( IOR as __ior_agg__ )

class Flag(__enum_flag__):
    ''' '''
    __blank__    = str()
    __fn_names__ = staticmethod(  __func_reduce__( __func_head__(map,__get_name__('__get_name__')), ' '.join ) )
    __fn_agg__   = staticmethod(__ior_agg__)
    @property
    def __get_names__(self):
        ''' '''
        return self.__fn_names__(self.__matches__)
    @property
    def __matches__(self):
        ''' '''
        return filter( __func_head__(__contains__,self), self.__class__ )
    @property
    def __get_name__(self):
        ''' '''
        return super().name or self.__blank__
    @property
    def name(self):
        ''' '''
        return self.__get_name__ or self.__get_names__
    @classmethod
    def Concat(cls, *flags):
        ''' '''
        return self.__fn_agg__(*flags)
