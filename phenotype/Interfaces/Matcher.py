from Partials  import Chain, map_partials, partial_lmap, pmap, rpartial, predicate_assign, has_attribute
from Yieldable import Yieldable
from re        import sub
from operator  import ( eq, contains )
from functools import ( partial )

class FuzzyMatch(object):
    ''' '''
    __slots__ = '_matches', '_size', '_source'
    def __init__(self, size, source, *matches):
        ''' '''
        self._matches = tuple(*matches)
        self._size    = size
        self._source  = source
    def __len__(self):
        ''' '''
        return len(self._matches)
    @property
    def Ratio(self):
        ''' '''
        return len(self) / self._size
    @property
    def Source(self):
        ''' '''
        return self._source
    def __repr__(self):
        ''' '''
        return f'{self.Ratio}'
    def __bool__(self):
        ''' '''
        return self.Ratio !=  0
    def __lt__(self, val):
        ''' '''
        return self.Ratio < val
    def __eq__(self, val):
        ''' '''
        return self.Ratio == val
    def __gt__(self, val):
        ''' '''
        return self.Ratio > val
    def __le__(self, val):
        ''' '''
        return self.Ratio <= val
    def __ge__(self, val):
        ''' '''
        return self.Ratio >= val

class FuzzyMatcher(object):
    ''' '''
    __proc_function__   = Chain( str.lower, str.split, partial_lmap( sub, '\W', '' ))
    __item_match_full__ = eq
    @classmethod
    def __item_match_partial__(cls, x, y):
        ''' '''
        return contains(y,x)
    @classmethod
    def __bind_matches__(cls, item_match, lookup):
        ''' '''
        return Chain( rpartial( pmap, map_partials(item_match,lookup) ), any )
    @classmethod
    def __match_function__(cls, source, item, lookup, partial_match):
        ''' '''
        item_match = cls.__item_match_partial__ if partial_match else cls.__item_match_full__
        size = len(lookup)
        pred = filter( cls.__bind_matches__(item_match, lookup), item)
        return FuzzyMatch( size, source, pred)
    def __init__(self, lookups=None, match_items=None, match_criteria=0.50, proc_function=None, match_function=None):
        ''' '''
        self._proc_function  = proc_function or self.__proc_function__
        self._match_function = match_function or self.__match_function__
    def __call__(self, item, lookup, partial_match=True) :
        ''' '''
        source = lookup
        item, lookup = map( self._proc_function, (item,lookup) )
        return self._match_function(source, item, lookup, partial_match)

class PartialMatch(object):
    ''' '''
    def __init__(self, source, match_function=None):
        ''' '''
        self._source         = source
        self._match_function = match_function or self.partial_match
    def __call__(self, item):
        ''' '''
        res = self._source.Where( self._match_function(item) )
        return res if len(res)  > 0 else item
    def __iter__(self) :
        ''' '''
        yield from self._source
    @staticmethod
    def partial_match(item):
        ''' '''
        proc_text    = Chain( str.lower, str.strip, lambda x : x.replace('"',''), str.split)
        get_text     = Chain( attrgetter('Text'), *proc_text )
        assign_items = predicate_assign( has_attribute('Text'), get_text, proc_text )
        items        = assign_items(item)
        match_pred = lambda source_item : any( (item in get_text(so)) )

        def lookup(source_item):
            ''' '''
            lookup_items = assign_items(source_item)
            return source_item if any( item in lookup_items for item in items ) else None
        return lookup
    @classmethod
    def InfoBoxMatcher(cls, items):
        ''' '''
        return cls( Yieldable(map(Parser,items), list), self.partial_match)
    @classmethod
    def ParsedTableColumn(cls, column):
        ''' '''
        return cls( Yieldable(chain(*Fn.lfil(column, lambda x : len(x) > 1))), self.partial_match)

class MultiKeyValue(set):
    ''' '''
    def __init__(self, keys, value):
        ''' '''
        key_iter = iter( (keys, ) ) if isinstance(keys,str) else iter(keys)
        super().__init__(key_iter)
        self.value = value
    def __eq__(self, key):
        ''' '''
        return key in self
class MultiLookup(object):
    ''' '''
    __slots__ = '_items', '_default'
    def __init__( self, multi_key_value_pairs, default=None):
        ''' '''
        self._items   = multi_key_value_pairs
        self._default = default
    def __contains__(self, key):
        ''' '''
        return next(filter( rpartial(contains, key), self._items) , None) is not None
    def __getitem__(self, key):
        ''' '''
        item = next( filter( rpartial(contains,key), self._items), None )
        return item.value if item is not None else self._default
    @classmethod
    def FromTuples(cls, *tuples, default=None):
        ''' '''
        items = [ MultiKeyValue(*t) for t in tuples ]
        return cls( items, default )
