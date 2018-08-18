if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
    # print(__sys_path__)
from operator import ( 
    attrgetter   as __op_attr_getter__,
    itemgetter   as __op_item_getter__,
    methodcaller as __op_method_caller__,
    eq           as __op_eq__,
    )
from Core.Incrementer import Incrementer
from Core.Get         import Item, Name

class Attributes:
    ''' '''
    @classmethod
    def Has(cls, name):
        ''' '''
        return rPartial(hasattr,name)
    @classmethod
    def Get(cls,name):
        ''' '''
        return __op_attr_getter__(name)
    @classmethod
    def GetD(cls, name, default=None):
        ''' '''
        return rPartial(getattr, name, default)
    @classmethod
    def Select(cls, *names):
        ''' '''
        return __op_attrg_etter__(tuple(names))
    @classmethod
    def SelectD(cls, *names, default=None):
        ''' '''
        selectors = map( rPartial(cls.GetD,default), names )
        return lambda item : tuple( ( s(item) for s in selectors ) )
class Items:
    ''' '''
    @staticmethod
    def Head(items):
        ''' '''
        return __op_item_getter__(0)(items)
    @staticmethod
    def Tail(items):
        ''' '''
        return __op_item_getter__(-1)(items)
    @staticmethod
    def LessHead(items):
        ''' '''
        return __op_item_getter__(slice(1,None))(items)
    @staticmethod
    def LessTail(items):
        ''' '''
        return __op_item_getter__(slice(None,-1))(items)
    @staticmethod
    def Pick(i):
        ''' '''
        def _pick(items):
            return __op_item_getter__(i)(items)
        return _pick
    @staticmethod
    def Take(i,j):
        ''' '''
        def _take(items): return __op_item_getter__(slice(i,j))(items)
        return _take
    @staticmethod
    def Select(*indices):
        ''' '''
        def _select(items): return __op_item_getter__(tuple(indices))(items)
        return _select
