from operator        import  methodcaller as __op_method_caller__

class Conditional(object):
    ''' '''
    __slots__ = ( 'predicate', 'function' )
    def __init__(self,predicate,function):
        ''' '''
        self.predicate = predicate
        self.function = function
    def filter(self,item):
        ''' '''
        return self.predicate(item)
    def __call__(self,item):
        ''' '''
        return self.function(item)
class IfElse(object):
    ''' '''
    __slots__ = ('predicate', 'true_function', 'false_function')
    def __init__(self, predicate, true_function, false_function):
        ''' '''
        self.predicate      = predicate
        self.true_function  = true_function
        self.false_function = false_function
    def __getitem__(self,key):
        ''' '''
        if isinstance(key,int): return getattr(self.__slots__[key],None)
    def __call__(self,item):
        ''' '''
        return self.true_function(item) if self.predicate(item) else self.false_function(item) 
class FirstTrue(object):
    ''' '''
    __slots__ = ( 'items', 'default' )
    def __init__(self, *items, default=lambda item : None):
        ''' '''
        self.items   = items
        self.default = default
    def __filter__(self,item):
        ''' '''
        condition = __op_method_caller__('filter',item)
        return next( filter( condition, self.items ), self.default )(item)
    def __call__(self,item):
        ''' '''
        return self.__filter__(item)

if __name__ == '__main__':
    ''' '''
    conditions = (Conditional( lambda x : x < 5, lambda x: x + 50), 
                Conditional( lambda x : x< 10 , lambda x : x**2 ),
                Conditional( lambda x : x, lambda x : [1,2] ))
    ft = FirstTrue(*conditions)
