if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
    from ResultContext import ResultContext
else:
    from .ResultContext import ResultContext
from collections    import ( defaultdict as __c_default_dict__ )
from functools      import ( wraps       as __ft_wraps__)
from itertools      import ( groupby     as __it_group__ )
from Access.Item    import Items, Names
from Func.Map       import Reducer
from Func.Partials  import Reduction, Head, Tail
from Predicate.Len  import Len

class Level:
    ''' '''
    __empty_level__ = staticmethod(lambda : list())
    __stored_as__   = list
    def __init__(self, tree, level, items, ordered):
        self._tree = tree
        self.level = level
        self.items = self.__empty_level__()
        self.order = [ordered]
        self.items.append( self.__stored_as__(items) )
    def __call__(self, items, ordered):
        ''' '''
        self.items.append( self.__stored_as__(items) )
        self.order.append(ordered)
    def __len__(self):
        ''' '''
        return len(self.items)
    def __get_sub_item__(self, index, bound):
        ''' '''
        encountered = self.order[index]
        if not bound: return self.items[index]
        elif encountered < bound: 
            sub_items = [self.items[index]]
            indices   = (i for i , x in enumerate(self.order[index+1:])  if x < bound  )
            for index in indices:
                sub_items.append(self.items[index])
            return sub_items
        else:
            return []
    def __getitem__(self, index):
        order = self.order[index:index+2]
        bound = order[1] if len(order) == 2 else None
        levels = []
        levels.append( (self.level, self.items[index] ))
        sub_levels = ( x for x in tuple(sorted( self._tree.Levels ) ) if x > self.level)
        for sl in sub_levels:
            levels.append( ( sl, self._tree[sl].__get_sub_item__( index, bound ) ) )
        return levels
class NestedLevel(object):
    ''' '''
    _items, _grouped = None, None
    @property
    def Keys(self):
        ''' '''
        return tuple( self._grouped.keys() ) if hasattr(self,'_grouped') else ( )
    def __init__(self, grouped_iterable, levels_remaining=0):
        ''' '''
        if levels_remaining == 0:
            self._items = ResultContext(grouped_iterable)
        else:
            self._grouped = grouped_iterable
            for k,v in self._grouped.items():
                setattr(self, k, Levels(v,levels_remaining-1))
    def __getitem__(self, name):
        ''' '''
        if name in self.__dict__: return self.__dict__[name]
        if self._items: return self._items.__getitem__[name]
        if self._grouped: return self._grouped.__getitem__[name]
    def __len__(self):
        ''' '''
        if self._items: return len(self._items)
        elif self._grouped: return len(self._grouped)
        else: return 0
    def __iter__(self):
        ''' '''
        if self._items: yield from self._items
        elif self._grouped: yield from self._grouped
        else: yield from ()
    def __getattr__(self, name):
        ''' '''
        if name in self.__dict__: return self.__dict__(name)
        elif self._items: self._items.__getattr__(name)
        elif self._grouped: return self._grouped[name]
        else: return None
class NestedGrouper(object):
    ''' '''
    def __init__(self, iterable, *group_bys):
        ''' '''
        self._group_levels, self.Levels = __create_nested_groups__(iterable, *group_bys )
    @classmethod
    def __create_nested_groups__(cls, iterable, *group_bys):
        ''' '''
        return ( len(group_bys) , Levels(cls.__nested_function__( iterable, *group_bys ), len(group_bys)  ) )
    @classmethod
    def __nested_function__(cls, iterable, *group_bys):
        ''' '''
        if Len.Less(2)(group_bys):
            return cls.__base_groupings__(iterable,group_bys)
        else:
            return cls.__recursive_nest__( __c_default_dict__(__c_default_dict__), iterable, [], group_bys )
    @classmethod
    def __recursive_nest__(cls, container, group_iter, keys, group_bys):
        ''' '''
        recursive_level = Len.More(1)(group_bys)
        grouper         = cls.__group_as__(group_bys)
        current_level   = cls.__nested_access__(container, keys)
        current_grouper = Items.Head(group_bys)
        #3 LOOP RECURISVELY
        for key, grouped in __it_group__( group_iter, current_grouper ):
            if recursive_level:
                #3 CREATE A NESTED DEFAULT DICT FOR UNMAPPED KEYS FOR RECURSIVE LEVELS
                if key not in current_level: current_level[key] = grouper()
                #3 FOR RECURSIVE CALL: i) APPEND CURRENT KEY TO EXISTING KEY SEQUENCE ii) DECREMENT CURRENT_GROUPER
                cls.__recursive_nest__( container, grouped, keys + [key], Items.LessHead(group_bys) )
            else:
                #3 MERGE GROUPED ITEMS AT NON-RECURSIVE LEVELS
                current_level[key].extend(group)
        return container
    #3 CONTAINER KEY ACCESSOR
    @staticmethod
    def __nested_access__(container, *keys):
        ''' '''
        return Reducer.Reduction( Reducer.Steps.NestedItemOnKeys, keys, container )
    @staticmethod
    def __group_as__(group_bys):
        ''' '''
        def __nested__(): return __c_default_dict__( __c_default_dict__)
        def __items__():  return __c_default_dict__( ResultContext )
        return __nested__ if Len.More(2)(group_bys) else __item__
    @classmethod
    def __base_groupings__(cls, iterable, groupbys):
        ''' '''
        return ResultContext.ConcatJoin( __it_group__(iterable, Items.Head(group_bys) ) ) if Len.Equal(1) else None
#2 CONCAT
class ConcatDict(dict):
    ''' '''
    def __init__(self, container_new, container_add, container_concat, *items):
        ''' '''
        self._container_new    = container_new
        self._container_add    = container_add
        self._container_concat = container_concat
        self.__concat_operation__(container_add)
        self.__concat_operation__(container_concat)
        super().__init__(self.__update__(*items))
    def __concat_operation__(self, operation):
        ''' '''
        @__ft_wraps__(operation)
        def __operation__(key, val): operation( self[key], val )
        name = f'{self._container_new.__name__}_{operation.__name__}'
        setattr(self, name, __operation__)
    def __getitem__(self, key):
        ''' '''
        if not super().__contains__(key): self.__setitem__(key, self._container_new() )
        return super().__getitem__(key)
    def __update__(self, other_dict=dict()):
        ''' '''
        for k, v in other_dict.items():
            ''' '''
            if isinstance(v,(str)) or not hasattr(v,'__iter__'):
                l = self._container_new()
                self._container_add(l,v)
                v = l
            elif not isinstance(v,self._container_new):
                ''' '''
                v = self._container_new(iter(v))
            yield (k,v)
    def update(self, *items):
        ''' '''
        for k,v in self.__update__(*items): self._container_concat(self[k],v)
        return self
    @classmethod
    def Concat(cls, base_dict, other_dict):
        ''' '''
        return base_dict.update(other_dict)
    @classmethod
    def List(cls, *items):
        ''' '''
        return cls( list, list.append, list.extend, *items )
    @classmethod
    def Set(cls, *items):
        ''' '''
        return cls( set, set.add, set.update, *items)
