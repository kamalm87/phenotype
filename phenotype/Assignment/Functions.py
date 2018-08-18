from operator import ( itemgetter as __op_item_getter__ )

class WrappedParameter:
    ''' '''
    __slots__ = ( 'parameter' )
    def __init__(self, parameter):
        ''' '''
        self.parameter = parameter
    def __call__(self, function):
        ''' '''
        return function(self.parameter)
    
def Sequence(*functions, return_as=tuple):
    ''' '''
    def _sequence(item): return_as( (fn(item) for fn in functions ) )
    return _sequence
def Items(*indices, return_as=tuple):
    ''' '''
    def _items(item): return return_as( ( g(item) for g in map(__op_item_getter__,indices) ) )
    return _items
def Filtered(iterable):
    '''Returns a filter of unary functions from the itereable'''
    def _filtered(item): return filter( WrappedParameter(item), iterable)
    return _filtered
