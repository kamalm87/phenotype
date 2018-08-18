from phenotype.Func import (
    __op_eq__,
    __func_partial__,
    )

class Instance(property):
    ''' '''
    #2 PUBLIC
    def add(self, instance):
        ''' '''
        self.__instances__.add(instance)
    #2 INTERNAL
    def __init__(self):
        ''' '''
        self.__instances__ = set()
        super().__init__()
    def __contains__(self, instance):
        ''' '''
        return instance in self.__instances__
    def __iter__(self):
        ''' '''
        yield from self.__instances__
    def __getitem__(self, instance):
        ''' '''
        return next(self.__match__(instance),None)
    def __get__(self, instance, owner=None):
        ''' '''
        return self[instance] if instance in self else self
    #2 CUSTOM
    def __predicate__(self, instance):
        ''' '''
        return __func_partial__( __op_eq__, instance )
    def __match__(self, instance):
        ''' '''
        return filter( self.__predicate__(instance), self ) 
