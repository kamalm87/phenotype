if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from itertools import (
    chain   as __it_chain__,
    starmap as __it_star_map__,
    )
from Access.Item     import Names    as __get_names__
from Access.Iterable import Iterable as __get_iter__
from Func.Partials   import (
    Head      as __func_head__,
    Tail      as __func_tail__,
    Reduction as __func_reduce__,
    )

class Interface:
    ''' '''
    __concat_reduction__ = None
    @classmethod
    def Concat(cls, *sequences):
        ''' '''
        return __func_reduce__.Reduction( cls.__concat_reduction__, sequences, cls() )
    @classmethod
    def Interpersed(cls, *items):
        ''' '''
        return cls( __it_chain__.from_iterable(items) )
    @classmethod
    def Mapped(cls, function):
        ''' '''
        return cls( map(function, cls) )
    @classmethod
    def MappedVariadic(cls, function, *items):
        ''' '''
        return cls( *__it_star_map__(function, items) )
    @classmethod
    def Selected(cls, predicate=None, function=None, *items):
        ''' '''
        mapper   = __func_head__( map, function) if function else iter
        filtered = filter(predicate, items)
        return cls( *mapper(filtered) )

class _Iterable:
    ''' '''
    __base_type__ = None
    def __yield_attr__(self,name):
        ''' '''
        yield from map(__get_names__.Get(name), self)
    def __getattr__(self, name):
        ''' '''
        return self.__base_type__(self.__yield_attr__(name))
    def __getitem__(self, key):
        ''' '''
        return self.__base_type.__getitem__(key)
    def __mapitem__(self, key, function):
        ''' '''
        item = self.__getitem__(key)
        if item:
            result = function(item)
            self.__setitem__(key,result)
    def __call__(self, function):
        ''' '''
        modifications = [ (i, function(v)) for i,v in enumerate(self) ]
        for key, mod in modifications:
            self.__setitem__(key,mod)
    def __iter__(self):
        ''' '''
        yield from self
class _Sequence(_Iterable):
    ''' '''
    __base_type__ = list
class _Bag(_Iterable):
    ''' '''
    __base_type__ = set
    def __getitem__(self, key):
        ''' '''
        if isinstance(key, int):
            slicer = __get_iter__.Pick(key)
        elif isinstance(key,slice):
            slicer = __get_iter__.Slicer( key.start, key.stop ) 
        else:
            slicer = __get_iter__.First( key )
        return slicer(self)
    def __setitem__(self, key, val):
        ''' '''
        item = self.__getitem__(key)
        if item is not None:
            self.__base_type__.remove(self, item)
        self.__base_type__.add(self, val)
    def __concat__(self, iterable):
        ''' '''
        self.__base_type__.update(self, iterable)
        return self
    def __remove__(self, iterable):
        ''' '''
        for item in iterable:
            self.__base_type__.discard(self,item)
        return self
    def __remove_where__(self, predicate):
        ''' '''
        for item in filter(predicate,self):
            self.__base_type__.discard(item)
        return self
    def __remove_at__(self, *indices):
        ''' '''
        indices = (indices,) if len(indices) == 0 else indices
        removals = reversed(sorted(filter(lambda index : index < len(self), indices)))
        for r in removals: 
            self.__base_type__.discard(self, self[r])
        return self
class _Mapping(_Iterable):
    ''' '''
    __base_type__ = set
    def __getitem__(self, key):
        ''' '''
        return super().__getitem__(key)
    def __setitem__(self, key, val):
        ''' '''
        super().__setitem__(key,val)
    def __mapitem__(self, key, function):
        ''' '''
        result = function(self[key])
        self[key] = result
