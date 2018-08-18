from phenotype.Core.Auxiliary import ( 
    __apply__,
    __identity__,
    )
def Lookup(key_func=__identity__,val_func=__identity__): return __apply__(key_func,val_func) 
class Hasher(dict):
    ''' '''
    __key_value_function__ = Lookup(id)
    __key__                = id
    @classmethod
    def __key_value__(cls, item):
        ''' '''
        return cls.__key_value_function__(item)
    def __init__(self, *items):
        ''' '''
        super().__init__( map( self.__key_value_function__, items ) )
    def __len__(self):
        ''' '''
        return len(self._mapping)
    def __contains__(self, item):
        ''' '''
        return self.__key__(item) in self._mapping.keys()
    def __iter__(self):
        ''' '''
        yield from self._mapping.items()
    def __getitem__(self, item):
        ''' '''
        hashed = self.__key__(item)
        return self.get(hashed,None)
    def __call__(self, item):
        ''' '''
        hashed = self.__key__(item)
        self._mapping[hashed] = item
        return hashed
