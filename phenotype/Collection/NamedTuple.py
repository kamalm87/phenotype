from itertools  import ( 
        chain   as __it_chain__,
        groupby as __it_group__,
        islice  as __it_slice__,
        starmap as __it_star_map__, )

class NamedTuple(object):
    ''' '''
    __slots__ = ()
    @classmethod
    def __len__(cls):
        ''' '''
        return len(cls.__slots__)
    @classmethod
    def FromIterable(cls, iterable):
        '''Maps up to the number of slots into the class's constructor from the iterable'''
        return cls( *__it_slice__(iterable, 0, cls.__len__()) )
    @property
    def __name__(self):
        ''' '''
        return self.__class__.__name__
    def __getitem__(self, index):
        '''Returns the attribute relating to the name in the class' slot index'''
        if index >= len(self):
            raise IndexError(f'Container has {len(self)-1} items, less than index: {index}')
        return getattr(self, self.__slots__[index] )
    def __iter__(self):
        ''' '''
        if not isinstance(self.__slots__, str):
            for name in self.__slots__:
                yield (name,getattr(self,name))
        else:
            yield ( self.__slots__, getattr(self, self.__slots__) )
    def __str__(self):
        ''' '''
        return str(tuple(self))
    def __repr__(self):
        ''' '''
        return str(self)
    def __init__(self, slot_names): pass
    def __new__(cls, name, slot_names):
        ''' '''
        name_tuple = type( name, (cls,), {})
