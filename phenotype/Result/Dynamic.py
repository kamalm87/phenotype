from itertools import ( zip_longest as __it_zip__ )

class _Container:
    ''' '''
    __slots__ = ( )
    def __getitem__(self,key):
        ''' '''
        if isinstance(key,int):
            return getattr(self, self.__slots__[key],None) if key < len(self.__slots__) else None
        elif isinstance(key,slice):
            ''' '''
            names = self.__slots__[key]
            return tuple( getattr(self,n,None) for n in names )
        elif isinstance(key,str):
            return getattr(self,key,None)
    def __getattr__(self,name):
        ''' '''
        if name in self.__slots__:
            return getattr(self,name)
    def __contains__(self, name):
        ''' '''
        return name in self.__slots__
    def __iter__(self):
        ''' '''
        yield from ( ( n, getattr(self,n) ) for n in self.__slots__ )
    def __len__(self):
        ''' '''
        return len(self.__slots__)
    @property
    def __keys__(self):
        ''' '''
        return self.__slots__
    @property
    def __values__(self):
        ''' '''
        return tuple( getattr(self,n) for n in self.__slots__ )
    @property
    def __name__(self):
        ''' '''
        return type(self).__name__
    def __repr__(self):
        ''' '''
        items = ', '.join( f'{n} : {v}' for n, v in self )
        return f'{self.__name__}({items})'

class Dynamic:
    ''' '''
    @classmethod
    def _dynamic_init(cls, default, *names):
        ''' '''
        def __init__(self, *args):
            ''' '''
            for n, v in __it_zip__(self.__slots__,args, fillvalue=default):
                setattr(self,n,v)
        return tuple(names), __init__
    @classmethod
    def Create(cls, name, *names, default=None):
        ''' '''
        members = {}
        members['__slots__'], members['__init__'] = cls._dynamic_init(default, *names)
        dynamic_type = type(name, (_Container,), members)
        return dynamic_type
