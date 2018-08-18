if __name__ == '__main__':
    from sys     import ( path    as __sys_path__ )
    from os.path import ( abspath as __abs_path__ )
    __sys_path__.insert(0, __abs_path__('..'))
from itertools import starmap as __it_starmap__
from operator    import ( 
    lt       as __lt__,
    le       as __le__,
    eq       as __eq__,
    ne       as __ne__,
    ge       as __ge__,
    gt       as __gt__,
    )
from Core.Get       import ( Name  as __get_name__ )
from Core.Auxiliary import ( Apply as __func_apply__ )

class Evaluator:
    ''' '''
    __slots__ = '_attributes'
    def __init__(self, attributes):
        ''' '''
        self._attributes = attributes
    def __values__(self):
        ''' '''
        return __func_apply__(*map(__get_name__,self._attributes))(self)
    def __evaluate__(self, other):
        ''' '''
        return zip( self.__values__(), other.__values__() ) 
    def __lt__(self, other):
        ''' '''
        return any( __it_starmap__(__lt__, self.__evaluate__(other) ) )
    def __le__(self, other):
        ''' '''
        return any( __it_starmap__(__le__, self.__evaluate__(other) ) )
    def __eq__(self, other):
        ''' '''
        return all( __it_starmap__(__eq__, self.__evaluate__(other) ) )
    def __ne__(self, other):
        ''' '''
        return all( __it_starmap__(__ne__, self.__evaluate__(other) ) )
    def __ge__(self, other):
        ''' '''
        return any( __it_starmap__(__ge__, self.__evaluate__(other) ) )
    def __gt__(self, other):
        ''' '''
        return any( __it_starmap__(__gt__, self.__evaluate__(other) ) )
