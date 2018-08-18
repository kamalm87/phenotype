from collections.abc       import Callable
from functools import reduce as __ft_reduce__
from phenotype.Access.Item import ( Names, Items )
from phenotype.Assignment.Assignment import IfElse
from phenotype.Core.Auxiliary        import Apply
from phenotype.Core.Components       import Executer
from phenotype.Func.Partials         import Reduction, Head, Tail
from phenotype.Func.Invoker          import Invoker

class Selector:
    ''' '''
    @staticmethod
    def Item(item): return item
    @staticmethod
    def Pair(first=Items.Pick(0),second=Items.Pick(1)): return Apply(first,second)
class Consumer(Callable):
    ''' '''
    def __init__(self,function):
        ''' '''
        self.function = function
    def __call__(iterable):
        ''' '''
        Executer(function,iterable)
class Mapper(Callable):
    ''' '''
    def __init__(self, function):
        ''' '''
        self.function = function
    def __call__(self, iterable):
        ''' '''
        yield from Executer.Map(self.function,iterable)

@Invoker
class Map:
    ''' '''
    FrozenSet = Reduction( map, frozenset )
    List      = Reduction( map, list )
    Tuple     = Reduction( map, tuple )
    Set       = Reduction( map, set )
    Dict      = Reduction( map, dict )
    @classmethod
    def Binary(cls, predicate, true_map, false_map):
        ''' '''
        logic = IfElse(predicate, true_map, false_map)
        def _map_binary(iterable):
            yield logic(iterable)
        return _map_binary
    @classmethod
    def Text(cls, iterable):
        ''' '''
        return map(str,iterable)
    @classmethod
    def If(cls, function, iterable, predicate=None):
        ''' '''
        return Reduction( Head( filter, predicate), Head( map, function ) )
    @classmethod
    def Where(cls, predicate, mappings, group=False, group_creator=list, group_join=list.append):
        ''' '''
        def _map(item): return mappings[predicate(item)](item)
        def _grouped(item):
            ''' '''
            group = predicate(item)
            return ( group, mappings[group](item) )
        def _map_where(iterable):
            ''' '''
            yield from map(_map,iterable)
        def _map_grouped(iterable):
            ''' '''
            def _group(iterable): yield from map( _grouped, iterable )
            _groups = dict()
            for grouping, items in _group(iterable):
                if grouping not in _groups: _groups[grouping] = group_creator()
                group_join( _groups[grouping], items )
            yield from ( (k, _groups[k] ) in _groups.keys() )
        return _map_where if not group else _map_grouped
    @classmethod
    def ToDict(cls, key_function, val_function, iterable=None, return_as=dict):
        ''' '''
        def _dict(iterable): yield from ( (key_function(item), val_function(item)) for item in iterable )
        def _as(iterable): return_as(_dict(iterable))
        return _as if iterable is None else _as(iterable)
    @classmethod
    def Consume(cls, mapped):
        ''' '''
        for item in mapped: pass
    @classmethod
    def Attributes(cls, name):
        ''' '''
        get = Names.Get(name)
        def _map_attributes(item):
            item = get(item)
            while item:
                yield item
                item = get(item)
        return _map_attributes
    @classmethod
    def Binary(predicate, true_function, false_function):
        ''' '''
        def _map(item): return true_function if predicate(item) else false_function
        return Head(map,_map)
@Invoker
class Yield:
    ''' '''
    @classmethod
    def All(cls, item):
        ''' '''
        yield item
        yield from item
    @classmethod
    def Item(cls, item):
        ''' '''
        yield item
    @classmethod
    def From(cls, item):
        ''' '''
        yield from item
    @classmethod
    def Binary(cls, predicate, items, include_item=True):
        ''' '''
        recurser = cls.All if include_item else cls.From
        yield from Map.Binary(predicate, cls.Item, recurser)(items)

@Invoker
class Reducer:
    ''' '''
    @classmethod
    def __call__(cls, *args):
        ''' '''
        return Head( Invoker.__reduction__, cls.Steps.FunctionalChain, args ) 
    @classmethod
    def Chain(cls, *methods):
        ''' '''
        return Head( Invoker.__reduction__, cls.Steps.FunctionalChain, methods ) 
    @staticmethod
    def Reduction( step, sequence, initial=None):
        ''' '''
        def _reduction(*args):
            ''' '''
            return __ft_reduce__(*args)
        return _reduction(step, sequence, initial)
    class Steps:
        ''' '''
        @staticmethod
        def NestedItemOnKeys(item, key):
            ''' '''
            return Items.Pick(key)(item)
        @staticmethod
        def FunctionalChain(item, invokable):
            ''' '''
            return invokable(item)
        @staticmethod
        def Concatenation(concat_function):
            ''' '''
            def _concatenation(reduction, item):
                ''' '''
                return concat_function( reduction, item )
            return _concatenation
        @staticmethod
        def Custom_Reduction_Then_Item( reduction_process, item_process, reducer):
            ''' '''
            def _custom( reduction, item ):
                ''' '''
                processed_reduction = reduction_process(reduction)
                processed_item = item_process(item) 
                return reducer( processed_reduction, processed_item )
            return _custom
        @staticmethod
        def Custom_Item_Then_Reduction( reduction_process, item_process, reducer):
            ''' '''
            def _custom( reduction, item ):
                ''' '''
                processed_item      = item_process(item)
                processed_reduction = reduction_process(reduction)
                return reducer( processed_item, processed_reduction )
            return _custom
