if __name__ == '__main__':
    from sys import path        as __sys_path__
    from os.path import abspath as __abs_path__
    __sys_path__.insert(0, __abs_path__('..'))
from enum            import auto, Enum, Flag
from Func.Aggregator import IOR

class ScaleProperty(Enum):
    ''' '''
    __limits__ = [ ]
    @property
    def Multipler(self): return self.__limits__[self.value]
    @property
    def Short(self): return str().join( filter(str.isupper, self.name) )
    @classmethod
    def __grouped_name__(cls): return { e.name : e for  e in cls }
    @classmethod
    def __grouped_value__(cls): return { e.value : e for  e in cls }
    @classmethod
    def __getitem__(cls, lookup):
        ''' '''
        if isinstance(lookup, int): return cls.__grouped_value__[lookup]
        if isinstance(lookup, str): return cls.__grouped_name__[lookup]
        return None

class FlagProperty(Flag):
    ''' '''
    __accumulator__ = IOR
    @classmethod
    def __maps_value__(cls):
        ''' '''
        return { e.value : e for e in iter(cls) }
    @classmethod
    def __maps_name__(cls):
        ''' '''
        return { e.name : e for e in iter(cls) }
    @classmethod
    def __getitem__(cls, value=None, name=None):
        ''' '''
        if value:
            return cls.__maps_value__().get(value)
        if name:
            return cls.__maps_name__().get(name)
    @classmethod
    def Accumulate(cls, *properties):
        ''' '''
        return cls.__accumulator__(*properties)
