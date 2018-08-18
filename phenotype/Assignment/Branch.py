if __name__ == '__main__':
    from Flow            import Flow
else:
    from .Flow import Flow

from collections.abc import ( Callable as __abc_callable__ )
class Branch(__abc_callable__):
    ''' '''
    __slots__ = ( '_flow' )
    def __init__(self, *predicate_assignments, default=None):
        ''' '''
        self._flow = Flow(*predicate_assignments, default=default)
    def __call__(self,item):
        ''' '''
        return self._flow[item]
