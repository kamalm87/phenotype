from phenotype.Assignment.Functions import ( 
    Filtered as __fn_filtered__ ,
    Items    as __fn_items__,)

class Flow(dict):
    ''' '''
    __items__ = __fn_items__(0,1) 
    @classmethod
    def __pair__(cls, iterable):
        ''' '''
        return map(cls.__items__,item)
    def __init__(self, *predicate_assignments, default= lambda item : None):
        ''' '''
        super().__init__( self.__pair__(predicate_assignments) )
        self.__default__ = default
    def __conditions__(self, item):
        ''' '''
        return __fn_filtered__(self.keys())(item)
    def __getitem__(self,item):
        ''' '''
        return next( self.__conditions__(item), self.__default__)(item)
    def __call__(self, item):
        ''' '''
        return self[item]
