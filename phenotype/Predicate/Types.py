def __invert__(predicate): lambda item : not predicate(item)

class Type(object):
    ''' '''
    @staticmethod
    def Has( name ):
        """Has intended to do something"""
        def _has(item): return hasattr( item, name )
        return _has
    @classmethod
    def HasNot(name):
        ''' '''
        return __invert__(cls.Has(name))
    @staticmethod
    def Match(instance_type):
        ''' '''
        def _match(item): return isinstance(item,instance_type)
        return _match
    @classmethod
    def Negate(cls, instance_type):
        ''' '''
        return __invert__(cls.Match(instance_type))
