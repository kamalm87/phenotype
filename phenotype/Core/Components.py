if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
    # print(__sys_path__)
from functools         import ( partial  as __ft_partial__, )
from itertools         import ( repeat   as __it_repeat__, )
from operator          import ( truth    as __op_truth__, )
from Assignment.Branch import Branch as __assignment_branch__
from .Defaults import Nullable

#2 DEFAULTS
class _Composer(object):
    ''' '''
    __slots__ = (  )
    @staticmethod
    def Repeat( n ):
        """Repeat intended to do duplicate argument ``n`` times"""
        def _repeat(item): return __it_repeat__( item, n )
        return _repeat 
    @staticmethod
    def ReturnAsParameter( parameter ):
        """ReturnAsParameter intended to do create a function that will always return a default value"""
        def _return_as_parameter_(*args,**kws): return parameter
        return _return_as_parameter_
class Defaults(object):
    ''' '''
    __slots__ = ( )
    @staticmethod
    def Identity(item):
        ''' '''
        return item
class Bindables(object):
    ''' '''
    __slots__ = (  )
    @staticmethod
    def Clone(n):
        ''' '''
        return _Composer.Repeat(n)
    @staticmethod
    def ReturnAsParameter( parameter ):
        """ReturnAsParameter intended to do something"""
        return _Composer.ReturnAsParameter(parameter)
    @staticmethod
    def AssignmentMap(**pred_assign_pairs):
        ''' '''
        return __assignment_branch__(*pred_assign_pairs, default=None)
    @staticmethod
    def Defaultable(predicate=__op_truth__, default=None):
        ''' '''
        def _defaultable(item): return item if predicate(item) else default
        return _defaultable
#2 DICTIONARY MAPPINGS
class KeyValue(object):
    ''' '''
    __slots__ = 'key', 'value'
    def __init__(self, key, value):
        ''' '''
        self.key   = key
        self.value = value
    def __len__(self):
        ''' '''
        return 2
    def __getitem__(self, index):
        ''' '''
        if index < len(self):
            return self.key if i == 0 else self.value 
        else:
            raise IndexError
    def __repr__(self):
        ''' '''
        return f'{self.key}\t{self.value}'
    @classmethod
    def Lookup(cls, value_function, key_function=Defaults.Identity):
        ''' '''
        def _lookup(item): return cls( key_function(item), value_function(item) )
        return _lookup
    @classmethod
    def DistinctHashable(cls, key):
        ''' '''
        if isinstance(key, (list,set,tuple)):
            return frozenset(key)
        elif isinstance( key, (dict)):
            return tuple( ( cls.DistinctHashable(k), cls.DistinctHashable(v)) for k,v in key.items() )
        else:
            return key
#2 INVOKERS
class _Executer(object):
    ''' '''
    __slots__ = (  )
    @classmethod
    def Consume(cls, iterable):
        ''' Consume uses iterable with the intent to: do something '''
        try:
            while True:
                next(iterable)
        except StopIteration:
            pass
    @classmethod
    def Mappable(cls, function):
        ''' '''
        return __ft_partial__( cls.Map, function )
    @classmethod
    def Map(cls, function, iterable):
        ''' '''
        yield from ( function(item) for item in iterable)
    def __call__(self, function, iterable):
        ''' '''
        self.Consume( map(function,iterable) ) 
Executer = _Executer()
