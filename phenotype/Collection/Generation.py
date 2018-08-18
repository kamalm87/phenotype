class Generation(object):
    ''' '''
    __slots__ = ('_source','_selection','_predicate')
    def __init__(self, source, selection, predicate=None):
        ''' '''
        self._source    = source
        self._selection = selection
        self._predicate = predicate
    def __iter__(self):
        ''' '''
        yield from map( self._selection, filter( self._predicate, self._source ) )
