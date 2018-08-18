from phenotype.Access import (
    _item_access as __get_item__,
    _name_access as __get_name__,
    _fn_head     as __func_head__,
    _fn_tail     as __func_tail__,
    _fn_reduce   as __func_reduce__ ,
    )
class Names:
    @classmethod
    def Get(cls,name,default=None):
        ''' '''
        return __get_name__(name,default)
    @classmethod
    def Select(cls, *names, default=None):
        ''' '''
        return __func_head__( map( __func_tail__(cls.Get,default) ) )
    @classmethod
    def SelectTuple(cls, *names, default=None):
        ''' '''
        return __func_reduce__( cls.Select(*names, default=default), tuple )
    @classmethod
    def SelectList(cls, *names, default=None):
        ''' '''
        return __func_reduce__( cls.Select(*names, default=default), list )
class Items:
    ''' '''
    @staticmethod
    def Head(items):
        ''' '''
        return __get_item__(0)(items)
    @staticmethod
    def Tail(items):
        ''' '''
        return __get_item__(-1)(items)
    @staticmethod
    def LessHead(items):
        ''' '''
        return __get_item__(slice(1,None))(items)
    @staticmethod
    def LessTail(items):
        ''' '''
        return __get_item__(slice(None,-1))(items)
    @staticmethod
    def Pick(i):
        ''' '''
        def _pick(items):
            return __get_item__(i)(items)
        return _pick
    @staticmethod
    def Take(i,j):
        ''' '''
        def _take(items): return __get_item__(slice(i,j))(items)
        return _take
    @staticmethod
    def Select(*indices):
        ''' '''
        def _select(items): return __get_item__(tuple(indices))(items)
        return _select
__doc__ = 'Index and attribute accessor static classes'
