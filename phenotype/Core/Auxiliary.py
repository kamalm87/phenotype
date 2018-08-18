from phenotype.Core import __abc_callable__

class _Identity(__abc_callable__):
    ''' '''
    def __init__(self): pass
    def __call__(self,item):
        ''' '''
        return item
Identity = _Identity()
class ReturnAs(__abc_callable__):
    ''' '''
    __slots__ = ( 'value' )
    def __init__(self,value):
        ''' '''
        self.value = value
    def __call__(self, *args, **kwargs):
        ''' '''
        return self.value
class Apply(__abc_callable__):
    ''' '''
    __slots__ = ( 'functions' )
    def __init__(self, *functions):
        ''' '''
        self.functions = functions
    def __iter__(self):
        ''' '''
        yield from self.functions
    def __call__(self, item):
        ''' '''
        return (fn(item) for fn in self) 
class TryExcept(object):
    ''' '''
    __slots__ = (  )
    @staticmethod
    def Unary(try_function,except_function=ReturnAs(None)):
        def _try_except_unary(item):
            try:
                return try_function(item)
            except:
                return except_function(item)
        return _try_except_unary
