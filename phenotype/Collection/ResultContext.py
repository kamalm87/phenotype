if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from collections import defaultdict as __c_default_dict__
from itertools  import ( 
        chain   as __it_chain__,
        groupby as __it_group__,
        islice  as __it_slice__,
        starmap as __it_star_map__, )
from Access.Item   import Items, Names
from Func.Map      import Yield, Map
from Core.Defaults import Nullable
from Func.Partials import ( Reduction )
from Predicate     import ( Filter, Len, )
class ResultContext(object):
    ''' '''
    __slots__ = '_items', '_container_type'
    def __init__(self, items=None, container_type=list):
        ''' '''
        self._container_type = container_type
        self._items = container_type( __it_chain__(iter(items)) ) if items else container_type()
    def __len__(self):
        ''' '''
        return len(self._items)
    def __getitem__(self, index):
        ''' '''
        if isinstance(index, int):
            return self._items[index] if Len.Least(index)(self) else Nullable
        else:
            return ResultContext(self._items[index])
    def __getattr__(self, name):
        ''' '''
        if Len.Most(1)(self):
            return Nullable if Len.Equal(0)(self) else Names.Get(name,Nullable)(Items.Head(self))
        else:
            return ResultContext(self.__get_name__(name))
    def __get_name__(self, name, default=Nullable):
        ''' '''
        return Filter.WithAttribute(name)(self)
    def __call__(self, function, on_first=False):
        ''' '''
        if Len.Most(1)(self):
            return Nullable if Len.Equal(0)(self) else function(self[0])
        else:
            return ResultContext( map( ResultContext( lambda c : function(c), self)))
    def __iter__(self):
        ''' '''
        yield from self._items
    def __repr__(self):
        ''' '''
        return repr(self._items)
    def __where__(self, pred):
        ''' '''
        yield from filter( pred, self )
    def __remove_at__(self, index_set):
        ''' '''
        for index, item in enumerate(self):
            if index not in index_set:
                yield item
    def where(self, pred=None):
        ''' '''
        return ResultContext( self.__where__(pred), container_type=self._container_type )
    def remove_where(self, pred=None):
        ''' '''
        self._items = self._container_type( self.__where__(pred) )
        return self
    def remove_at(self, *indices):
        ''' '''
        index_set = set(indices)
        self._items = self._container_type( self.__remove_at__(index_set) )
        return self
    def prepend(self, item):
        ''' '''
        self._items = self._container_type( __it_chain__( [item], self ) )
    def append(self, item):
        ''' '''
        self._items.append(item)
    def extend(self, iterable):
        ''' '''
        self._items.extend(iterable)
    @classmethod
    def __is_result__(cls, item):
        ''' '''
        return Prop.Sequence(item)
    @property
    def __flat__(self):
        ''' '''
        yield from Yield.Binary( self.__is_result__, self )
    @property
    def Get(self):
        ''' '''
        if Len.Most(1):
            return Nullable if Len.Equal(0)(self) else Items.Head(self)
        else:
            return self
    @property
    def Tail(self):
        ''' '''
        return Items.Tail(self)
    @property
    def Flat(self):
        ''' '''
        return ResultContext( self.__flat__, self._container_type )
    @property
    def Nested(self):
        ''' '''
        return any( map( self.__is_result__, self ) )
    @staticmethod
    def _Concat_Default_Dict(reduction, item ):
        ''' '''
        group, join_with = Items.Select(0,1)(item)
        group(reduction).extend(join_with)
        return reduction
    @classmethod
    def ConcatJoin( grouped_iter, group_container=__c_default_dict__):
        ''' '''
        return Reduction.Reduction( cls._Concat_Default_Dict, grouped_iter, group_container( cls ) )
