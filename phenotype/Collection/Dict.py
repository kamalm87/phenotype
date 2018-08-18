from functools  import ( 
        partial  as __ft_partial__,
        reduce   as __ft_reduce__,
        wraps    as __ft_wraps__)
from itertools  import ( 
        chain   as __it_chain__,
        groupby as __it_group__,
        islice  as __it_slice__,
        starmap as __it_star_map__, )

class Dict(dict):
    ''' '''
    def __init__(self, *key_value_pairs):
        ''' '''
        super(Dict, self).__init__( iter(key_value_pairs) )
    def __add__(self, key_value_pair):
        ''' '''
        self[ key_value_pair[0] ] = key_value_pair[1]
    def __iadd__(self, mapping):
        ''' '''
        return self.update(mapping)
    def update(self, mapping):
        ''' '''
        super(Dict, self).update(mapping)
        return self
    @classmethod
    def Concat(cls, *mappings):
        ''' '''
        return __ft_reduce__(Dict.update, mappings, Dict())
    @classmethod
    def Mapped(cls, function, *key_value_pairs):
        ''' '''
        return cls( *__it_starmap__(function, key_value_pairs) )
    @classmethod
    def Selected(cls, predicate=None, function=None, *key_value_pairs):
        ''' '''
        mapper   = __ft_partial__(__it_starmap__,function) if function else iter
        filtered = filter(predicate, key_value_pairs)
        return cls( *mapper(filtered) )
