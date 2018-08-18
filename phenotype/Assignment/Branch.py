from phenotype.Assignment      import __abc_callable__
from phenotype.Assignment.Flow import Flow

class Branch(__abc_callable__):
    '''Returns the first function correspondingly mapped to a predicate that evalutes
        as true based on unary input
    '''
    __slots__ = ( '_flow' )
    def __init__(self, *predicate_assignments, default=None):
        ''' ``predicate_assignments``: predicate/function pairs '''
        self._flow = Flow(*predicate_assignments, default=default)
    def __call__(self,item):
        ''' '''
        return self._flow[item]
__doc__ = 'Flow-control done via a dictionary'
